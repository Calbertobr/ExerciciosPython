#!/bin/python
from os import system
from time import sleep
system('clear')
def Manual( Com ):
    help( Com )


def Titulo( msg , cor=0 ):
    tm = len( msg ) + 4
    print(f'\033[0;{cor}m')
    print('~' * tm)
    print(f'  {msg}')
    print('-' * tm)
    print('\033[m')


##
Comando = ''
while Comando != 'fim' :
    system('clear')
    Titulo('Systema de ajuda PyHelp.',36)
    Comando = str(input('  Digite o nome do comando que deseja o relp: ')).lower()
    if Comando != 'fim':
        Titulo(Comando,31)
        Manual(Comando)
    else:
        Titulo('Ate Logo',31)
    

