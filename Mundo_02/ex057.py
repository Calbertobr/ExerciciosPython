#!/bin/python
# Digia o sexo e verifica se esta correto F/M ate acertar.
from os import system
system('clear')

Sexo = str(input('Digite o sexo: [M/F]')).upper().strip()[0]

while  Sexo != 'F' and Sexo != 'M' :
    Sexo = str(input('Por favor digite seu sexo: [M/F]')).upper().strip()[0]
print('Seu sexo e {}.'.format(Sexo))
    