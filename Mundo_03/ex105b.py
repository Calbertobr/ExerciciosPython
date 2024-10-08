#!/bin/python
#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas, – A maior nota, – A menor nota, – A média da turma, – A situação (opcional)

from os import system
system('clear')

def notas(* n, Sit=False):
    Dic={}
    Dic['Maior'] = max(n)
    Dic['Menor'] = min(n)
    Dic['Quant'] = len(n)
    Dic['Media'] = sum(n)/len(n)
    if Sit:
        if Dic['Media'] >= 7 :
            Dic['Situação'] = 'Boa'
        elif 5 <= Dic['Media'] < 7 :
            Dic['Situação'] = 'Razoável'
        else:
            Dic['Situação'] = 'Ruin'
    return Dic





resp = notas(2.5,6.3,2.5,7.5,6.5,9.1,5.8,Sit=True)
print(resp)
resp = notas(4,6,8,9,4,6)
print(resp)
resp = notas(3,9,Sit=True)
print(resp)