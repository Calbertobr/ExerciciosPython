#!/bin/python
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

from os import system
system('clear')
def ficha(no='',go=''):
        """
        no nome do jogador
        go Numero de gols
        """
        if no.strip() == '':
                no = '<Desconhecido>'
        if go.isnumeric() :
                go = int(go)
        else:
                go = 0
        print(f'O jogador {no} fez {go} gol(s) no campeonato')

Nome = input('Nome do jogador: ')
Gols = input('Numero de gols: ')

ficha(Nome,Gols)
#help(ficha)