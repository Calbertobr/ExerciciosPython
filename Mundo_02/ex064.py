#!/bin/python

# Ler varios numeros interios e parar quando digitar 999 mostrar quantos numero e a soma deles.

from os import system
system('clear')
num = 0
cont = -1
soma = 0
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite o numero: '))

print("""
A quantidade de numeros e {}.
A soma dos numero e igual {}.
""".format(cont,soma))