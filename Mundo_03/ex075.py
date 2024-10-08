#!/bin/python

from os import system
system('clear')
Lista = (int(input('Digite o primeiro numero: ')),
         int(input('Digite o segundo numero: ')),
         int(input('Digite o quarto numero: ')),
         int(input('Digite o quinto numero: ')),
        )
#for a in range(0,4):
#    Num[a] = int(input(f'Digite o {a}º valor: '))
#
#Lista = (Num[0],Num[1],Num[2],Num[3])

print(f' O numero 9 aparece {Lista.count(9)} vezes.')
if Lista.count(3) > 0:
    print(f' O numero 3 aparece na posição {Lista.index(3)}.')
else:
    print(f' O numero 3 não aparece na lista.')

ct = 0
for a in Lista :
    if a % 2 == 0 :
        ct +=1

print(f' Na lista existe {ct} numeros pares.')

