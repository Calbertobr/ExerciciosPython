#!/bin/python

# inseri um numero interio e mostra a serie de fibonacci

from os import system
system('clear')

Termos = int(input('Digite a quantidade de termos de fibonacci: '))
c = 0
Fib = 0
Fib2 = 1
Fib3 = 0

while c < Termos :
    print('{:2} {:3}'.format(c+1,Fib),end='')
    print('')
    Fib3 = Fib2
    Fib2 = Fib
    Fib = Fib2+Fib3
    c += 1