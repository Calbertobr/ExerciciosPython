#!/bin/python
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
from os import system
system('clear')
def escreva(texto):
    comp = ( len(texto)+8 )//2
    print('-='*comp)
    print(f'--- {texto} ---')
    print('-='*comp)
a = str(input('Digite o texto: '))
escreva(a)
