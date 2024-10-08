#!/bin/python
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from os import system
from random import randint
system('clear')

Jogador = dict()
Jogo = []
JogoEnd = []
for j in range(0,6) :
    Jogador['nome'] = str(f'Jogador {j+1}º')
    Jogador['jogada'] = randint(1,6)
    Jogo.append(Jogador.copy())

for a in Jogo :
    print(f' {a["nome"]}  {a["jogada"]}. ')

JogoEnd = sorted(Jogo,key=lambda j: j['jogada'] ,reverse=True)

for i, b in enumerate(JogoEnd) :
    print(f'{i+1}º Lugar: {b["nome"]} com {b["jogada"]} ')


