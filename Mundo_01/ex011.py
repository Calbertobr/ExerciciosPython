#!/bin/python3

import os
os.system('clear') or None

# forneca a altura e a largura de uma parede calcule a area e quanto de tinta precisa para pintar
# Sabe se que cada litro de tinta pinta 2m²

l1 = float(input('Qual a largura da Parede em metros: '))
a1 = float(input('Qual a altura da Parede em metros : '))

print('\nA area total a ser pintada e de {:.2f}m² e sera nescessario {:.2f}l de tinta'.format((a1*l1),(a1*l1/2))+'\n')
