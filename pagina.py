from flask import Flask, render_template, request #importa os módulos do flask
from chatterbot import ChatBot # importa o chatbot
from chatterbot.trainers import ListTrainer # importa o método de treino
import os

alan = ChatBot('Alan') # inicia o bot

treinador = ListTrainer(alan) # define o método de treino
app = Flask(__name__) # inicia a aplicação flask

value = "Olá" 

for arquivo in os.listdir(r'chats'): # percorrer todos os arquivos
	linhas = open(r'chats/' + arquivo, 'r').readlines() # ler todas as linhas
	treinador.train(linhas) # treina o conteúdo das linhas


@app.route('/pagina.py',)
@app.route('/',)
def hello():
    try:
        msg = request.args.get('mensagem', value) # recebe a mensagem do usuário

        resposta = alan.get_response(msg) # gera uma resposta
        if float(resposta.confidence) >= 0.3: # verifica se a resposta tem mais de 30% de confiança
            return render_template('index.html', **{'alan': resposta}) # retorna a resposta
        else:
            return render_template('index.html', **{'alan': 'Desculpe, ainda não sei responder essa pergunta'}) # Resposta padrão 
    except Exception as e:
        return render_template('index.html', **{'Alan': 'Ocorreu um erro durante a execução:'+e}) # Retorna mensagem de erro


if __name__ =='__main__':
    app.run() # Inicia a aplicação