from os import system
from random import choice
system('clear')


Lista = []
for a in range(1,5):
    Lista.insert(a,input('Digite o nome do aluno '))

escolhido = choice(Lista)

print('O escolhido foi :{}'.format(escolhido))

