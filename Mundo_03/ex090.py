#!/bin/python
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
from os import system
system('clear')
Aluno = dict()
Alunos = []

Continue = 's'
while Continue != 'n' :
    Aluno['nome'] = str(input('Nome do aluno: ')).strip()
    Aluno['media'] = float(input('Qual a Media: '))
    if Aluno['media'] >= 7 :
        Aluno['status'] = 'Aprovado'
    elif 5 <= Aluno['media'] < 7 :
        Aluno['status'] = 'Recuperação'
    else:
        Aluno['status'] = 'Reprovado'
    Alunos.append(Aluno.copy())
    Continue = str(input('Deseja continuar [s/n] ?')).strip()[0]

#Alunos = [{'nome': 'carlpos', 'media': 9.0, 'status': 'A'}, {'nome': 'jorge', 'media': 6.0, 'status': 'R'}]
print(Alunos)

for aluno in Alunos :
    print(f'O aluno {aluno["nome"]} teve media {aluno["media"]} e por isso esta com status {aluno["status"]}.')
