#!/bin/python

from os import system
system('clear')
Lista = []
Continue = 's'
while Continue != 'n' :
    Valor = int(input('Digite o numero: '))
    if Valor not in Lista :
        Lista.append(Valor)
        print('Valor adicionado com sucesso..')
    else:
        print('Valor Duplicado.')
    Continue = str(input('Deseja Continuar: [s/n]:' )).strip().lower()[0]
    #if Continue == 'n' :
    #    break
Lista.sort()
print(f'A lista em ordem e {Lista}')

