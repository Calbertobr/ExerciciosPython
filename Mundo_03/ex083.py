#!/bin/python
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
from os import system
system('clear')
Pa = 0
Eque = str(input('Digite uma expreesão matematica: ')).strip()
for a in Eque :
    if a == '(' :
        Pa += 1
    elif a == ')' :
        Pa -= 1

if Pa == 0 :
    print('Equção Valida. ')
else:
    print('Equação Invalida ')

print(Eque)