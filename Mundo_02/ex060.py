#!/bin/python

# Leia um numero e mostre os termos do fatoria

from os import system
system('clear')

num = int(input('Digite o numero para calcular o fatorial: '))
Mult = 1
print('{}!= '.format(num),end='')
while 0 != num :
    Mult *= num
    if num != 1:
        print('{}x'.format(num),end='')
    else:
        print('{}'.format(num),end='')
    num -= 1
print(' = {}'.format(Mult))