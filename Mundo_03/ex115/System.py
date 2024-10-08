#!/bin/python3.11
MenuData = ['Ver pessoa cadastrada','Cadastrar nova pessoa','Remover Cadastro','Sair do sistema']
from lib.interface import *
from lib.arquivo import *
from time import sleep
import os

while True :

    resposta = menu(MenuData)
    if resposta == 1 :
        cabecalho('Opção - 1')
        FileRead()
        sleep(3)
        
    elif resposta == 2 :
        cabecalho('Opção - 2')
        FileInclude()
        sleep(1)
    elif resposta == 3 :
        cabecalho('Opção - 3')
        FileDelete()
        sleep(1)
    elif resposta == 4 :
        cabecalho('Opção - 4')
        break
    else:
        print('\033[31m Digite opção valida \033[m')
        sleep(2)
