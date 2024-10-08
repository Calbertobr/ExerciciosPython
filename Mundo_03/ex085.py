#!/bin/python
#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
from os import system
system('clear')
Lista = [[],[]]
for a in range(0,7) :
    Num = int(input(f'Digite o {a}º numero: '))
    if Num % 2 == 0 :
        Lista[0].append(Num)
    else:
        Lista[1].append(Num)
Lista[0].sort()
Lista[1].sort()
print(f'Lista de numeros pares {Lista[0][:]}')
print(f'Lista de numeros impares {Lista[1][:]}')


