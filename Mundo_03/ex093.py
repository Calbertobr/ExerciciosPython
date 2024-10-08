#!/bin/python
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
from os import system
system('clear')

Jogadores = list()
Jogador = dict()
Gols = list()
Continue = 's'
while Continue != 'n' :
    
    Jogador['nome'] = str(input('Qual o nome do jogador: ')).strip()
    Jogador['Jogos'] = int(input('Quantas partidas jogou: '))
    for j in range(0,Jogador['Jogos']) :
        Gols.append(int(input(f'Quantos gols fez na {j+1}º partida ')))
    Jogador['golsjogos'] = Gols[:]
    Jogador['mediaGol'] = sum(Gols)/Jogador['Jogos']
    Jogadores.append(Jogador.copy()) 
    Continue = str(input('Deseja continuar [s/n]: '))

for Jog in Jogadores :
    print(f'O aproveitamenro medio do jogador {Jog["nome"]}\nCom seus {Jog["Jogos"]} jogos e de {Jog["mediaGol"]} gols por jogo')


