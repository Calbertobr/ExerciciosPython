#!/bin/python

from os import system
system('clear')

count = soma = 0
while True:
    num = int(input('Digite os numeros, para parar digite 999: '))
    if num == 999:
        break
    count +=1
    soma += num
print(f'Foram digitados {count} numeros e soma e igual a {soma}')