#!/bin/python

# ler dois valore e mostra opções de [ + ] [ - ] [ * ]  [ / ]  [ Maior ] [ Novos ]  e [ sair ]

from os import system
system('clear')

Num1 = float(input('Digite o primeiro numero: '))
Num2 = float(input('Digite o segundo numero: '))
Opcao =''
while Opcao != '0': 
    system('clear')
    print("""
    [ + ] Somar
    [ - ] Subtrair 
    [ * ] Multiplicar
    [ / ] Dividir
    [ > ] Maior numero
    [ N ] Digitar novos numeros
    [ 0 ] Sair
    """)
    if Opcao == '+':
        print('A soma dos valores e Igual a {:.2f}.'.format(Num1 + Num2)) 
    elif Opcao == '-':
        print('A subtração dos valores e Igual a {:.2f}.'.format(Num1 - Num2))
    elif Opcao == '*':
        print('A multiplicação dos valores e Igual a {:.2f}.'.format(Num1 * Num2)) 
    elif Opcao == '/':
        print('A divisão dos valores e Igual a {:.2f}.'.format(Num1 / Num2)) 
    elif Opcao == '>':
        if Num1 > Num2 :
            print('O primeiro numero {} e maior que o segundo {}.'.format(Num1,Num2))
        else :
            print('O primeiro numero {} e menor que o segundo {}.'.format(Num1,Num2))
    elif Opcao == 'N':
        Num1 = float(input('Digite o primeiro numero: '))
        Num2 = float(input('Digite o segundo numero: '))


    Opcao =  str(input('Digite a opção: ')).strip()

    