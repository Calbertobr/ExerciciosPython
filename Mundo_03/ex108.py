#!/bin/python
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from os import system
system('clear')

import ex107_moeda as moeda

preco = float(input('Qual o valor do produto: '))

print(f'O do produto de valor {moeda.moeda(preco,False)} com seu dobro passa a se de { moeda.moeda(moeda.dobro( preco ),True) }' )
print(f'O do produto de valor {moeda.moeda(preco,True)} tendo a metade do valor igual a { moeda.moeda(moeda.metade( preco ),True)}' )
print(f'O do produto de valor {moeda.moeda(preco,True)} tendo 10% de desconto passa ao valor de { moeda.moeda(moeda.desconto( preco,10 ),True)}')
print(f'O do produto de valor {moeda.moeda(preco,True)} tendo 15% de aumento passa ao valor de { moeda.moeda(moeda.aumento( preco,15 ),True ) }')
