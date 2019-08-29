from flask import Flask, make_response #importa os módulos do flask
from chatterbot import ChatBot # importa o chatbot
import os

alan = ChatBot(
    'Alan',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe, ainda não sei responder essa questão.',
            'maximum_similarity_threshold': 0.50
        },
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///db.sqlite3'
) # inicia o bot

app = Flask(__name__) # inicia a aplicação flask

@app.route('/<string:user>')
def hello(user):
    try:
        msg = alan.get_response(user) # gera uma resposta
        resposta = make_response(str(msg))
        resposta.headers['Access-Control-Allow-Origin'] = '*'
        return resposta, 200 # Retorna a resposta do bot

    except Exception as e:
        erro = 'Ocorreu um erro durante a execução:',e
        resposta = make_response(erro)
        resposta.headers['Access-Control-Allow-Origin'] = '*'
        return resposta, 200 # Retorna mensagem de erro

if __name__ =='__main__':
    app.run() # Executa a aplicação