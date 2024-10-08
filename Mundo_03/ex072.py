#!/bin/python

from os import system
system('clear')

Numbers = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = 99
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num >= 0 and num <= 20 :
        print(f'O numero digitado {num} e {Numbers[num]}')
    #elif num < 0 :
        break;


