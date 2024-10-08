#!/bin/python

from os import system
system('clear')

while True:
    Mul = 0
    num = int(input('Qual tabuada deseja ?' ))
    
    if num <= 0:
        break
    while Mul < 11:
        print(f'{Mul:3} * {num:3} = {num*Mul:3}')
        Mul +=1