#!/bin/python
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from os import system
system('clear')

#import utilidade.moeda as moeda
from utilidade import moeda as moeda, dado as dado
from os import system
system('clear')

preco = float(input('Valor a ser analisado: '))
system('clear')
moeda.resumo(preco,80,50)
