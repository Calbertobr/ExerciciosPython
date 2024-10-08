#!/bin/python
#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
from os import system

system('clear')
def maior(* num):
    print('-'*20)
    a = mai = 0
    print(f'A lista fornecida de {len(num)} numeros a seguir: ',end='')
    for a in num :
        print(f' {a}',end='')
        if mai < a :
            mai = a



    print(f'\nO maior numero dela e {mai}.')
Data = []
maior(10,25,36,95,20,12,43,52,2,0,8,52,36,9)
maior(2,5,9,3,1,4)
maior(10,5,3)
maior(3,5,9)
maior()