#!/bin/python3
import os
os.system('clear') or None

# Leia um salario do funcionario e mostre o novo com 15% de aumento.

s1 = float(input('Qual o salario do funcionario: '))

print('O salario do funcionario com 15% de aumento passa a ser de R$ {}'.format( (s1 * 115)/100 ))