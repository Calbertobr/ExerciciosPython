#!/bin/python

from os import system
from math import hypot
system('clear')


co = float(input('Qual a medida do cateto oposto: '))
ca = float(input('Qual a medida do cateto adjacente: '))


# 1
# hi = (ca**2 + co**2)**(1/2) 

#2
hi = hypot(co,ca)

print('O valor da hipotenusa e de: {:.2f}'.format(hi))


