#!/bin/python
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

from os import system
system('clear')
Impar = []
Par = []
Lista = []
Continue = 's'
while Continue != 'n' :
    num = int(input('Digite um numero: '))
    Lista.append(num)
    Continue = str(input('Deseja continuar: [s/n] ')) 
for b in Lista :
    if b % 2 == 0 :
        Par.append(b)
    else:
        Impar.append(b)
print(f'A lista de numeros pares e ')
for a in Par :
    print(f' {a}',end='')
print('.')
print(f'A lista de numeros impares e ')
for a in Impar :
    print(f' {a}',end='')
print('.')
print(f'A lista de total de numeros e ')
for a in Lista :
    print(f' {a}',end='')
print('.')