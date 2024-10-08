#!/bin/python

# Ler o primeiro termo a razo e calcular dez termos da pa

from os import system
system('clear')

Termo = int(input('Digite o termo: '))
Razao = int(input('Digite a Razao: '))
c = 1
while c < 11:
    print('{:2} {:3}'.format(c,Termo))
    Termo = Termo + Razao
    c +=1 