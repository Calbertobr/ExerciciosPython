#!/bin/python
#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

from os import system
def area(larg,comp):
    area = larg * comp
    print(f'A area de {larg} x {comp} e igual {area:.2f}m²')
def line():
    print('-='*20)

system('clear')
line()
a = float(input('Digite a largura (m): '))
b = float(input('Digite o Comprimento (m): '))
line()
area(a,b)
line()

