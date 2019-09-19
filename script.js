function pegaResposta() { // Função que faz a requisição e gera as mensagens
    var mensagem = document.getElementById("message_input").value; // recebe o valor digitado pelo usuário
    let url = "http://localhost:5000/" + mensagem; // define a url de conexão com a API

    criaMensagem(mensagem, "b"); // cria a mensagem do usuário
    var xhttp = new XMLHttpRequest(); // define o objeto
    xhttp.open("GET", url, true); // faz a requisição na API

    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) { // verifica se a requisição ocorreu e se deu certo
                criaMensagem(xhttp.responseText, "a"); // cria a mensagem do chatbot
            }
        }

        xhttp.send(); // garante que o programa continue rodando mesmo se ocorrer uma falha nha requisição
}

function criaMensagem(conteudo, classe){ // Função que cria a mensagem
    if (classe == "a") { // Verifica se a mensagem foi enviada pelo usuário
        var mensagem = '<div class="msg_sent a"><p class="mensagem">'+conteudo+'</p></div>'; // cria uma mnensagem com o conteúdo do usuário
        } else {
            var mensagem = '<div class="msg_sent b"><p class="mensagem">'+conteudo+'</p></div>'; // cria uma mnensagem com o conteúdo do chatbot
        }

    $("ul").append(mensagem).scrollTop($("ul").prop('scrollHeight')); // adiciona a mensagem dentro da tag UL da página
}