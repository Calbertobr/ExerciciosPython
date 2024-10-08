#!/bin/python
#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from os import system
system('clear')
Continue = 's'
Alunos = []
Aluno = []
Nota = []
while Continue != 'n' :
    Nome = str(input('Nome do Aluno: '))
    Nota.append(float(input('Digite a primeira nota: ')))
    Nota.append(float(input('Digite a segunda nota: ')))
    Nota.append( ( Nota[0] + Nota[1] ) / 2 )
    Aluno.append(Nome[:])
    Aluno.append(Nota[:])
    Alunos.append(Aluno[:])
    Nota.clear()
    Aluno.clear()
    Continue = str(input('Deseja Continuar [s/n] : '))


for Nome, Notas in Alunos :
    print(f'O aluno de nome {Nome} teve media  {Notas[2]} ')

Continue = 's'
while Continue != 'n' :
    Pesquisa = input('Digite o nome do aluno: ').strip().lower()
    for Nome, Notas in Alunos :
        if str(Nome).lower() == Pesquisa :
            print(f'O aluno de nome {Nome} teve as notas {Notas[0]} e {Notas[1]} e sua media e {Notas[2]} ')
    Continue = str(input('Deseja Continuar [s/n] : '))
