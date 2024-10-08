#!/bin/python
#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from os import system
from random import randint
system('clear')
Jogos = int(input('Digita a quantidade de palpites: '))
ListaJogos = []
ListaJogo = []
for x in range(0,Jogos) :
    while len(ListaJogo) != 6 :
        Val = randint(1,60)
        if Val not in ListaJogo :
            ListaJogo.append(Val)
    ListaJogo.sort()
    ListaJogos.append(ListaJogo[:])
    ListaJogo.clear()
for jogo in range(0,len(ListaJogos)) :
    print('-='*30)
    print(ListaJogos[jogo])
    print('-='*30)
    for l in range(0,60,10) :
        for c in range(1,11) :
            P = (l+c)
            if P in ListaJogos[jogo] :
                print(f'  \033[0;31;41m{P:2}\033[m  ',end='')
            else:
                print(f'  {P:2}  ',end='')
        print()


