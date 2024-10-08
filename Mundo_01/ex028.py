#!/bin/python
from random  import randint
from os import system
system('clear')
print('-=-'*10)
print(':::Teste sua Sorte ::::')
print('-=-'*10)
sort = randint(0,5)
num = int(input('Digite um numero entre 0 e 5: '))

if num == sort :
    print('Voce acertou.... Parabens....')
else:
    print('Não foi desta vez....')
