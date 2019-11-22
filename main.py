# instalar no terminal cmd o pip3 e o chatterbot para a execucao deste programa IA.
#sudo pip3 install chatterbot

#-*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer # impotando o treinador.
from chatterbot import ChatBot # importando o chatbot.
import os # importando o os.

bot = ChatBot('Teste') # criando o charbot com o nome teste.

bot.set_Trainer(Listtrainer) # setando o metodo de treinamento.

for arq in os.listdir('arq'): # listando os arquivos que tem dentro da pasta arq.
	chats = open('arq/' + arq, 'r').readlines() # carregando as conversas que tem dentro do arq.
	bot.train(chats)
	
while True:
	resq = input('Você: ')
	
	resp = bot.get_response(resq)
	print('Bot: ' + str(resp))
