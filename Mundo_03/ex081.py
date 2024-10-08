#!/bin/python
#Crie um programa que vai ler vários números e colocar em uma lista.
#   Depois disso, mostre:
#    A) Quantos números foram digitados.
#    B) A lista de valores, ordenada de forma decrescente.
#    C) Se o valor 5 foi digitado e está ou não na lista.

from os import system
system('clear')

Lista = []
Continue = 's'
while Continue != 'n' :
    Num = int(input('Digite um numero: '))
    Lista.append(Num)
    Continue = str(input('Desja continuar [s/n]: ')).strip().lower()[0]
print(Lista)
print(f'Foram digitados {len(Lista)} numeros.')
print(f'A lista de valores ordenada e ',end='')
for a in sorted(Lista,reverse=True) :
    print(f' {a}',end='')
print('.')

if 5 not in Lista :
    print('O numero cinco não foi encontrado entre os digitados. ',)
else:
    print('O numero cinco foi encontrado entre os digitados, posição : ',end='')
    for i, c in enumerate(Lista) :
        if c == 5 :
            print(f' {i}',end='')
    print()

