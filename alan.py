from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

alan = ChatBot('Alan')

treinador = ListTrainer(alan)

for arquivo in os.listdir(r'chats'): # percorrer todos os arquivos
	linhas = open(r'chats/' + arquivo, 'r').readlines() # ler todas as linhas
	treinador.train(linhas)

while True:
	try:
		msg = str(input("Diga Algo: "))

		resposta = alan.get_response(msg)
		if float(resposta.confidence) >= 0.3:
			print("Alan:",resposta)
		else:
			print("Alan: Desculpe, ainda não sei como responder")
	except Exception as e:
		print("Erro :", e)
		break
