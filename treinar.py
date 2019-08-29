from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from server import alan
import os

treinador = ListTrainer(alan)

for arquivo in os.listdir(r'chats'): # percorrer todos os arquivos
	linhas = open(r'chats/' + arquivo, 'r').readlines() # ler todas as linhas
	treinador.train(linhas) # treina o conteúdo das linhas