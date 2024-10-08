# Criar tabuada de um numero informado
from os import system
system('clear')

base = int(input('Qual o numero que deseja a sua tabuada: '))

for a in range(0,11):
    print('{:2} x {:2} = {:3}'.format(base,a,(a*base)))