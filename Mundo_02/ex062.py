#!/bin/python

# o mesmo anterior mas pergunta se quer mostrar mais termos e quantos- se digitar 0 finaliza

from os import system
system('clear')

Termo = int(input('Digite o termo: '))
Razao = int(input('Digite a razão: '))
Termos = 10
while Termos != 0:
    count = 0
    Termoc = Termo
    while count != Termos:
        print(' {:3}'.format(Termoc),end='')
        Termoc += Razao
        count +=1
    Termos = int(input('\n\nDesja mais termos, ou 0 para sair:'))
