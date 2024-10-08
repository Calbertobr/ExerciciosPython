#!/bin/python
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from os import system
system('clear')

StatusVoto = ('Negado','Opcional','Obrigatorio')
def voto( ano = 1900 ):
    from datetime import datetime
    global Idade
    Idade = datetime.now().year - ano
    if Idade < 16 :
        return 0 
    elif ( Idade >=16 and Idade < 18 ) or Idade >= 65 :
        return 1
    elif Idade >= 18 and Idade < 65 :
        return 2
Idade = 0
Data = int(input('Informe sua data de nascimento: '))

Retorno = voto(Data)

print(f'De acordo com as leis braseleiras sua idade e {Idade} seu status e {StatusVoto[Retorno]} ')
