# Sistema de Votação Eletrônica

## Objetivo do Sistema
O Sistema de Votação Eletrônica foi desenvolvido para coletar opiniões políticas e níveis de satisfação dos eleitores em relação aos candidatos, promovendo uma maneira interativa e segura de consolidar os dados para análise.

## Instruções para Iniciar o Sistema Localmente

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/Leonsilveira/sistema-de-votacao.git

   Navegue até o diretório do projeto:
   cd sistema-de-votacao
   
Instale as dependências: Certifique-se de que você tenha o Python instalado em sua máquina. Em seguida, instale as dependências listadas no arquivo :
pip install -r requirements.txt

Inicialize o banco de dados: Execute o backend para criar automaticamente o banco de dados SQLite:
python app.py

Acesse o sistema: O servidor será iniciado localmente em http://127.0.0.1:5000 e em seguida va ate a aba e adcione ao final /resultados . 
Abra essa URL no navegador para interagir com o sistema.

Requisitos para Rodar


## Requisitos
- **Python** 3.7 ou superior
- **Flask** (backend)
- **Chart.js** (biblioteca de gráficos)
- **SQLite** (banco de dados)

## Estrutura do Projeto
- `app.py`: Backend do sistema
- `index.html` e `index2.html`: Frontend
- `templates/`: Templates HTML
- `static/`: Arquivos CSS, JS e imagens
- `requirements.txt`: Dependências do projeto

## Funcionalidades
- Coleta de opiniões e satisfações dos eleitores
- Geração de gráficos interativos
- Interface amigável e moderna

