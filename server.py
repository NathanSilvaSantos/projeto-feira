from flask import Flask, render_template, request, jsonify, make_response #importa os módulos do flask
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


@app.route('/<string:user>')
def hello(user):
    try:
        msg = alan.get_response(user) # gera uma resposta
        if float(msg.confidence) >= 0.3: # verifica se a resposta tem mais de 30% de confiança
            resposta = make_response(str(msg))
            resposta.headers['Access-Control-Allow-Origin'] = '*'
            return resposta, 200 # Retorna a resposta do bot
        else:
            resposta = make_response('Desculpe, ainda não sei responder essa pergunta')
            resposta.headers['Access-Control-Allow-Origin'] = '*'
            return resposta, 200 # Resposta padrão 
    except Exception as e:
        erro = 'Ocorreu um erro durante a execução:',e
        resposta = make_response(erro)
        resposta.headers['Access-Control-Allow-Origin'] = '*'
        return resposta, 200 # Retorna mensagem de erro

if __name__ =='__main__':
    app.run() # Executa a aplicação