#!/bin/python
#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
from os import system
system('clear')

Matriz = [[0,0,0],[0,0,0],[0,0,0]]

for x in range(0,3):
    for y in range(0,3):
        Num = int(input(f'Digite o item da cordenada x{x} x y{y}: '))
        Matriz[x][y] = Num


for x in Matriz :
    print(f' [{x[0]:^6}]  [{x[1]:^6}]  [{x[2]:^6}] ')
    