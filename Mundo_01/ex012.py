#!/bin/python3
import os
os.system('clear') or None

# Forneca o preço de um produto e calcule o seu novo preço com desconto de 5%

n1 = float(input('\nQual o valor do produto a ser calculado o desconto: '))

print('\nO valor do produto que e de R$ {} passa a custar com o desconto de 15% e de R$ {}'.format(n1,(n1*0.85))+'\n')
