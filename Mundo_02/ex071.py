#!/bin/python

from os import system
system('clear')

#50:20:10:1

Valor = int(input('Qual o valor do saque: '))
Cedulas = [50,20,10,5,1]

for a in Cedulas :
    QtdCedula = Valor // a
    print(Valor)
    print(f'{QtdCedula:3} Cedulas de {a:4} total de {QtdCedula*a:4}. ')
    Valor = Valor % a
