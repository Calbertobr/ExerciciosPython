#!/bin/python
from os import system
system('clear')
Lista = []
for a in range(0,10) :
    num = int(input(f'Digite o {a+1}° numero.'))
    if a == 0 or num > Lista[-1] :
        Lista.append(num)
    elif num < Lista[0] :
        Lista.insert(0,num)
    else :
        pos = 0
        while pos < len(Lista) :
            if num <= Lista[pos] :
                Lista.insert(pos,num)
                break
            pos += 1    
print(Lista)    