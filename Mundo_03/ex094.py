#!/bin/python
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
from datetime import datetime
from os import system
system('clear')
Continue = 's'
Pessoa = {}
Pessoas = []
while Continue != 'n' :
    Pessoa['nome'] = str(input('Qual o nome: ')).strip()
    while True :
        Pessoa['sexo'] = str(input('Qual o Sexo [f/m]: ')).strip().lower()[0]
        if Pessoa['sexo'] in 'mf' :
            break    
        print('Digite apenas [m/f]')
    Pessoa['idade'] = int(input('Anos de nascimento: '))
    Pessoas.append(Pessoa.copy())
    Continue = str(input('Deseja continuar [s/n]: '))
#Pessoas = [{'nome': 'Carlos', 'sexo': 'm', 'idade': 1970}, {'nome': 'Adriana', 'sexo': 'f', 'idade': 1970}, {'nome': 'Gabriela', 'sexo': 'f', 'idade': 2004}, {'nome': 'Manuela', 'sexo': 'f', 'idade': 2007}]
Subn = 0
for a in Pessoas :
    Subn += datetime.now().year - a['idade']
Media = Subn / len(Pessoas)
print(f'A quantidade de pessoas no cadastro: {len(Pessoas)}')
print(f'A media de idade no grupo e de {Media:.1f} anos.')
print('A mulheres deste grupo são: ',end='')
for p in Pessoas :
    if p["sexo"] == 'f' :
        print(f'{p["nome"]}  ', end='')
print()
print('As pessoas a seguir tem idade acima da media: ',end='')
for p in Pessoas :
    if ( datetime.now().year - p['idade'] ) > Media :
        Idade = datetime.now().year - a['idade']
        print(f'{p["nome"]} ',end='')
print()