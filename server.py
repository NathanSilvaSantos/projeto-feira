from flask import Flask, make_response #importa os módulos do flask
from chatterbot import ChatBot # importa o chatbot

alan = ChatBot(
    'Alan', # nome do chatbot
    storage_adapter='chatterbot.storage.SQLStorageAdapter', # define a linguagem do banco de dados
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch', # seleciona sempre a melhor resposta
            'default_response': 'Desculpe, ainda não sei responder essa questão.', # resposta padrão
            'maximum_similarity_threshold': 0.50 # porcentagem máxia de confiança para ser chamada a resposta padrão
        },
        'chatterbot.logic.MathematicalEvaluation' # permite que o chatbot faça cálculos simples
    ],
    database_uri='sqlite:///db.sqlite3' # define o banco de dados
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