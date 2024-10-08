#!/bin/python
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

from os import system
system('clear')

def fat(fator=1,show=False) :
    """
    Fatorial:
    para calcular fatorial
    fator:  Valor a ser calculado
    Show:   (Opcional) Se desaja mostrar o calculo [s/n]
    """
    fat = 1
    i = 2
    Resolv = ' 1'
    while i <= fator :
        Resolv = f' {i} *' + Resolv 
        fat = fat *i
        i += 1
    if show == True :
        print(f'A solção e :\n{fat}! = {Resolv} = {fat}')
    else:
        return fat

#

Num = int(input('Digite o numero: '))
#mostrar = str(input('Digite se desja ver o calculo: [s/n]')).strip()[0]

fat(Num,True)
print('~'*20)
Dat = fat(Num*2)
print(Dat)