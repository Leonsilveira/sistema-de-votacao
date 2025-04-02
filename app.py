import os
from flask import Flask, request, jsonify, render_template
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Caminho do banco de dados
DB_PATH = "db/enquete.db"

# Garantir que a pasta db exista
if not os.path.exists("db"):
    os.makedirs("db")

# Criando o banco de dados se não existir
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS enquete (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            estado TEXT NOT NULL,
                            opiniao TEXT NOT NULL,
                            avaliacoes TEXT NOT NULL)''')
        conn.commit()

# Rota para salvar respostas da enquete
@app.route("/salvar", methods=["POST"])
def salvar():
    dados = request.get_json()
    estado = dados.get("estado")
    opiniao = dados.get("opiniao")
    avaliacoes = str(dados.get("avaliacoes"))

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO enquete (estado, opiniao, avaliacoes) VALUES (?, ?, ?)", (estado, opiniao, avaliacoes))
        conn.commit()
    
    return jsonify({"success": True, "message": "Enquete salva com sucesso!"})

# Rota para listar todas as respostas
@app.route("/listar", methods=["GET"])
def listar():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM enquete")
        registros = cursor.fetchall()
    
    return jsonify({"success": True, "dados": registros})

# Rota para mostrar os resultados de votação
@app.route("/resultados", methods=["GET"])
def resultados():
    # Conectando ao banco de dados
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT opiniao, COUNT(*) FROM enquete GROUP BY opiniao")
        resultados = cursor.fetchall()

    # Organizando os resultados por categoria
    categorias = ['Presidente', 'Senador', 'Governador', 'Prefeito']
    votos = {categoria: {} for categoria in categorias}
    
    for categoria in categorias:
        for resultado in resultados:
            opiniao, count = resultado
            votos[categoria][opiniao] = count
    
    return render_template('index2.html', votos=votos)

# Inicializa o banco de dados
init_db()

# Para o Vercel
def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run(debug=True)
