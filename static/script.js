document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("button"); // Botão de envio

    form.addEventListener("click", function (event) {
        event.preventDefault(); // Impede o envio padrão do formulário

        const estado = document.getElementById("state").value;
        const opiniao = document.getElementById("view").value;

        // Captura as avaliações dos políticos
        const avaliacoes = {};
        ["presidente", "senador", "governador", "prefeito"].forEach((cargo) => {
            const radios = document.getElementsByName(cargo);
            for (let radio of radios) {
                if (radio.checked) {
                    avaliacoes[cargo] = radio.value;
                    break;
                }
            }
        });

        // Validação
        if (!estado || !opiniao || Object.keys(avaliacoes).length < 4) {
            alert("Por favor, preencha todos os campos antes de enviar.");
            return;
        }

        // Criando objeto para armazenar os dados
        const dados = {
            estado,
            opiniao,
            avaliacoes,
        };

        console.log("Respostas coletadas:", dados);
        alert("Enquete enviada com sucesso!");
        
        // Aqui você pode enviar os dados para um servidor ou salvar localmente
        // Exemplo: localStorage.setItem("enquete", JSON.stringify(dados));
    });
});

document.querySelector("button").addEventListener("click", function(event) {
    event.preventDefault();

    // Pegando os valores dos inputs
    const estado = document.getElementById("state").value;
    const opiniao = document.getElementById("view").value;
    
    // Pegando os valores de avaliação
    const avaliacoes = {
        presidente: document.querySelector('input[name="presidente"]:checked')?.value,
        senador: document.querySelector('input[name="senador"]:checked')?.value,
        governador: document.querySelector('input[name="governador"]:checked')?.value,
        prefeito: document.querySelector('input[name="prefeito"]:checked')?.value,
    };

    // Verifica se todas as opções foram preenchidas
    if (!estado || !opiniao || Object.values(avaliacoes).includes(undefined)) {
        alert("Por favor, preencha todos os campos!");
        return;
    }

    // Enviando os dados via fetch
    fetch('http://127.0.0.1:5000/salvar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            estado: estado,
            opiniao: opiniao,
            avaliacoes: avaliacoes
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Enquete salva com sucesso!");
        } else {
            alert("Erro ao salvar a enquete.");
        }
    })
    .catch(error => {
        console.error("Erro:", error);
        alert("Erro de conexão.");
    });
});
