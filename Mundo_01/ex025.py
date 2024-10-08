#!/bin/python

from os import system
system('clear')

nome = str(input('Digite Nome completo: ')).strip()

print('O nome tem silva: {}'.format('SILVA' in nome.upper()))
