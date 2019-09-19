# Importações
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from server import alan # importa o objeto que será treinado
import os

treinador = ListTrainer(alan) # define o método de treino

# Treinamento
for arquivo in os.listdir(r'chats'): # percorrer todos os arquivos da pasta
	linhas = open(r'chats/' + arquivo, 'r').readlines() # ler todas as linhas
	treinador.train(linhas) # treina o conteúdo das linhas