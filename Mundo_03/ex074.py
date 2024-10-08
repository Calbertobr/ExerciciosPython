#!/bin/python
from random import randint
from os import system
system('clear')
Tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(Tupla)
print(f'O numero menor e {min(Tupla)} e o maior e {max(Tupla)}.')


