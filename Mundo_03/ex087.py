#!/bin/python
#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

from os import system
system('clear')
Matriz = [[0,0,0],[0,0,0],[0,0,0]]
for x in range(0,3):
    for y in range(0,3):
        Num = int(input(f'Digite o item da cordenada x{x} x y{y}: '))
        Matriz[x][y] = Num
print(Matriz)
Soma = 0
SomaTer = 0
MaxSeg = 0
Par = 0
x = 0
y = 0
for x in range(0,3) :
    for y in range(0,3) :
        Soma += Matriz[x][y]
        if Matriz[x][y] % 2 == 0 :
            Par += Matriz[x][y]
        if y == 2 :
            SomaTer += Matriz[x][y]
        if x == 1 :
            if Matriz[x][y] > MaxSeg :
                MaxSeg = Matriz[x][y]
for x in Matriz :
    print(f' [ {x[0]} ]  [ {x[1]} ]  [ {x[2]} ] ')
print(f'A soma de todos os valore e {Soma}.')
print(f'A soma dos numeros pares e {Par}.')
print(f'A soma dos termos da terceira coluna e {SomaTer}.')
print(f'O maior valor da segunda linha e {MaxSeg}')