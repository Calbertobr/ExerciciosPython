#!/bin/python

# Acertar um numero dado pelo computador e contar quantas vezes errou ate acertar 0 ~10

from os import system
system('clear')

from random import randint
Cpu = randint(1,10)
Jogada= 999
Cnt = 0
while Jogada != Cpu :
    Jogada = int(input('Digite seu palpite: '))
    Cnt +=1
print('Voce acertou numero {}, apos {} Jogadas.'.format(Jogada,Cnt))