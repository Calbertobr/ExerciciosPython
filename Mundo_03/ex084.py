#!/bin/python
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

from os import system
system('clear')
"""Turma=[['Jonas',23,96],['Margot',18,102],['Fred',17,90],['Mary',15,44],['Inali',14,58],['Grace',12,75],['Meg',22,70]] """
Continue = 0
Pessoa = []
Turma = []
print('-='*30)
while Continue != 'n' :
    Pessoa.append(str(input('Nome: ')).strip())
    Pessoa.append(int(input('Idade: ')))
    Pessoa.append(int(input('Peso: ')))
    Turma.append(Pessoa[:])
    Pessoa.clear()
    Continue = str(input('Deseja continuar a cadstrar: [s/n]')).lower().strip()[0]


print(f'Foram cadastradas {len(Turma)} pessoas')
PesoTot = 0
for a, b, c in Turma :
    PesoTot += c
PesoMed = PesoTot / len(Turma)

print(f'Considerando peso medio de {PesoMed:.2f} kg.')
print(f'Temos as seguinte pessoas com peso menor que a media: ',end='')
for a, b, c in Turma :
    if c <= PesoMed :
        print(f' {a} com {c}Kg ',end='')
print()
print(f'Temos as seguinte pessoas com peso acima da media: ',end='')
for a, b, c in Turma :
    if c > PesoMed :
        print(f' {a} com {c}Kg ',end='')
print()