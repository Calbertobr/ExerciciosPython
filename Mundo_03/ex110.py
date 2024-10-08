#!/bin/python
# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

import ex107_moeda as moeda
from os import system
system('clear')

preco = float(input('Valor a ser analisado: '))
system('clear')
moeda.resumo(preco,20,25)
