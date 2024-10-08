#!/bin/python

#LEia varios numeros e depois mostre quantos, media, minimo maximo.

from os import system
system('clear')

num = 0
Cont = -1
Soma = 0
Min = 9999999
Max = 0
while num != 999:
    Soma += num
    if num < Min and Cont >= 0 :
        Min = num
    if num > Max :
        Max = num
    Cont +=1
    num = float(input('Digite numero: '))

print("""
Foram digitados {} numeros.
O menor numero e {}
O maior numero e {}
E a media dele e {}
""".format(Cont,Min,Max,Soma/Cont))