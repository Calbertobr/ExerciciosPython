#!/bin/python
from os import system
system('clear')

frase = str(input('Digite uma frase: ')).strip()
letra = input('Selecione a letra a pesquisar: ')
Frase = frase.upper()
Letra = letra.upper()
print('A frase tem {} carcteres'.format(len(Frase)))
print('Existe {} letras {}.'.format(Frase.count(Letra),letra))
print('A primeira começa na posição {}.'.format(Frase.find(Letra)+1))
print('A ultima na posição {}.'.format(Frase.rfind(Letra)+1))
