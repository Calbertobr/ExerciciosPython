#!/bin/python
#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from os import system
system('clear')

import ex107_moeda as moeda

preco = float(input('Qual o valor do produto: '))

print(f'O do produto de valor {moeda.moeda(preco,False)} com seu dobro passa a se de { moeda.dobro( preco,True ) }' )
print(f'O do produto de valor {moeda.moeda(preco,True)} tendo a metade do valor igual a { moeda.metade( preco, True )}' )
print(f'O do produto de valor {moeda.moeda(preco,True)} tendo 10% de desconto passa ao valor de {moeda.desconto(preco,10,True)}')
print(f'O do produto de valor {moeda.moeda(preco,True)} tendo 15% de aumento passa ao valor de {moeda.aumento(preco,15,True)}')
