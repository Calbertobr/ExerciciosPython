#!/bin/python3

# Receba um numero e mostre sua tabuada.

n1 = float(input('Digite o numero que deseja a tabuada: '))

print('A tabuada do numero {}.'.format(n1))
print('_'*20)

i = 0

for i in range(0,11):
    print(' {:>2} * {:>5} = {:>5}'.format(i,n1,(n1*i)))

