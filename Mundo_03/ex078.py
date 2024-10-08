#!/bin/python

from os import system
system('clear')
Lista = []
Mai = 0
Men = 0
Maip = 0
Menp = 0
for a in range(0,5):
    Lista.append(int(input(f'Digite o {a+1}º valor: ')))
    if a == 0 :
        Mai = Men = Lista[a]
    else:
        if Lista[a] < Men :
            Men = Lista[a]
        if Lista[a] > Mai :
            Mai = Lista[a]
print(Lista)
print(f'1 - O maior numero e {max(Lista)} e sua posição na lista e {Lista.index(max(Lista))}.')
print(f'1 - O menor numero e {min(Lista)} e sua posição na lista e {Lista.index(min(Lista))}.')

print(f'2 - O valor menor e {Men} e o sua posição e ',end='')
for p, b in enumerate(Lista) :
    if b == Men :
        print(f' {p}',end='')
print('.')


print(f'2 - O valor maior e {Mai} e o sua posição e ',end='')
for p, b in enumerate(Lista):
    if b == Mai :
        print(f' {p}',end='')
print('.')