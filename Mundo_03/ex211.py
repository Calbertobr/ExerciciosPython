#!/bin/python
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

from os import system
system('clear')

def leiaint(msg):
    Tipo = 0
    while Tipo != 1: 
        x = input(msg)
        if x.isnumeric():
            x = int(x)
            return x
        else:
            print('\033[0;31mErro: Digite um numero valido!! \033[m')


w = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {w}')