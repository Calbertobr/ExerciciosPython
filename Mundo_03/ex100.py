#!/bin/python
#  Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from os import system
from random import randint
system('clear')

def sorteia(Qtd):
    print('-'*20)
    for a in range(0,Qtd):
        Lista.append(randint(1,10)) 
    print(f' Quantidade de registros: {len(Lista)}')
    print(f' Lista: {Lista}')
        
def Somapar(b):
    print('-'*20)
    Soma = 0
    for a in b :
        if a % 2 == 0 :
            Soma += a
    print(f' A foma dos numeros pares e de {Soma}')
    print(f' Media igual: {sum(Lista)/len(Lista):.2f}')
    

Lista = []
#sorteia(randint(1,20))
sorteia(5)
Somapar(Lista)
