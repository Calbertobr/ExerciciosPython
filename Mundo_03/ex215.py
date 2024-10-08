#!/bin/python3.11

# Crie um programa modular
# Opções 1 Listar pessoas Cadastradas
#        2 Cadastrar nova pessoa.
#           - Nome completo
#           - Idade
#        3 Sair do sistema
#
#       Os dados devem ser gravados em um arquivo.
#

import os

Db = '/home/calbertobr/dados.db'

def borda( ):
    os.system('clear')
    print(40*"=")

def Listar():
    data = open(Db,'r')
    borda()
    for nome, idade in data:
        print(f'{nome}  {data}')
    data.close()

def cadastro():
    try:
        Nome = str(input("Nome completo: "))
    except (ValueError):
        print('Dados incorretos.')
        cadastro()
    try:
        Idade= int(input("Qual a idade: "))
    except (ValueError):
        print('Idade Invalida.')
        data = open(Db,'r')
        data.write(f'{Nome}|{Idade}')
        data.close()

borda()
Lista = """
        1 - Listar cadastro.
        2 - Para novo Cadastro.
        3 - Sair do Sistema.
"""

try:
    print(Lista)
    Opc = int(input('Digite a opão a:'))
except (ValueError):
    print('O valor a ser digitado deve concidir com a lista')

if Opc == 2:
    cadastro()
if Opc == 1:
    Listar()
