from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

alan = ChatBot('Alan')

treinador = ListTrainer(alan)
app = Flask(__name__)

value = "Olá"

def treinar():
    for arquivo in os.listdir(r'chats'): # percorrer todos os arquivos
	    linhas = open(r'chats/' + arquivo, 'r').readlines() # ler todas as linhas
	    treinador.train(linhas)


@app.route('/pagina.py',)
@app.route('/',)
def hello():
    treinar()
    try:
        msg = request.args.get('mensagem', value)

        resposta = alan.get_response(msg)
        if float(resposta.confidence) >= 0.3:
            return render_template('index.html', **{'alan': resposta})
        else:
            return render_template('index.html', **{'msg': msg})
    except Exception as e:
        return render_template('index.html', **{'msg': e})


if __name__ =='__main__':
    app.run()