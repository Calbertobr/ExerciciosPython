#!/bin/python
from random import randint
from os import system
system('clear')

Vitoria = Jogadas = 0
while True:
    system('clear')
    print('-=-'*10)
    print('Jogo de par ou impar.')
    print('-=-'*10)
    Cpu = randint(0,20)
    if Jogadas > 0 :
    
        if ( Cpu + Numero ) % 2 == 0 :
            print('Acertou')
            Vitoria += 1
        else:
            print('Errou...')
            break
    Numero =  int(input('Digite o numero: '))
    Escolha = str(input('Par ou Impar [P/I]')).upper().strip()[0]
    Jogadas += 1
print(f'De {Jogadas} jogadas voce acertou {Vitoria}.')