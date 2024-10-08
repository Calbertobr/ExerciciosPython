#!/bin/python
#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas, – A maior nota, – A menor nota, – A média da turma, – A situação (opcional)

from os import system
system('clear')

def notas(* n,Sit=False) :
    """
    n Valores das notas
    Sit Situação do aluno perante a sua media
        False não mostra 
        True Mostra a situação
        Return mostraos dados do aluno
    """
    Dic = {}
    Situcao = ('Ruin','Regular','bom')
    Dic['Media'] = 0
    Dic['Quantidade'] = len(n)
    Dic['Maior'] = 0
    Dic['Menor'] = 10
    for a in n :
        if a > Dic['Maior'] :
            Dic['Maior'] = a
        if a < Dic['Menor'] :
            Dic['Menor'] = a   
        Dic['Media'] += a 
    Dic['Media'] = Dic['Media'] / Dic['Quantidade']
    if Sit == True :
        if Dic['Media'] < 5 :
            Dic['Situação'] = Situcao[0]
        elif 5 <= Dic['Media'] < 7 :
            Dic['Situação'] = Situcao[1]
        elif Dic['Media'] >= 7 :
            Dic['Situação'] = Situcao[2]
    print('-'*20)
    print(Dic)

notas(2.5,6.3,2.5,7.5,6.5,9.1,5.8,Sit=True)
notas(4,6,8,9,4,6)
notas(3,9,Sit=True)
help(notas)