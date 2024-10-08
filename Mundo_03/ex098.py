#!/bin/python
#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) uma contagem personalizada

from os import system
from time import sleep
system('clear')
print('-='*20)

def contador(Start,Stop,Step): 
    if Step < 0 :
        Step *= -1
    if Step == 0 :
        Step = 1
    print(f'Contando de {Start} ate {Stop} com passo de {Step}')
    sleep(1)
    cont = Start 
    if Start < Stop :
        while cont <= Stop :
            print(f' {cont}',end='',flush=True)
            sleep(0.1)
            cont += Step
        print(' Fim.')
    else:
        while cont >= Stop :
            print(f' {cont}',end='',flush=True)
            sleep(0.1)
            cont -= Step 
        print(' Fim.')
    print()
    print('-='*20)

contador(1,10,1)
contador(10,0,2)
ini = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
paso = int(input('Digite o passo: '))
contador(ini,fim,paso)

