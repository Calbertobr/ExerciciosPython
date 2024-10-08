#!/bin/python
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import ex107_moeda as moeda



preco = float(input('Qual o valor do produto: '))

print(f'O dobro do valor do produto e de R$ {moeda.dobro(preco)}')
print(f'A metade do valor do produto e de R$ {moeda.metade(preco)}')
print(f'O aumento de 10% do valor do produto e de R$ {moeda.aumento(preco,10)}')
print(f'A redução de 15% do valor do produto e de R$ {moeda.desconto(preco,15)}')
