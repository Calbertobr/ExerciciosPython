#!/bin/python
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from os import system
from datetime import datetime
system('clear')

Empregados = []
Empregado = dict()

Continue = 's'
while Continue != 'n' :
    Empregado['nome'] = str(input('Nome do colaborador: '))
    Empregado['anasc'] = int(input('Qual o ano de nascimento: '))
    Empregado['idade'] = datetime.now().year -  Empregado['anasc']  
    Empregado['ctps'] = int(input('Qual  numero da CTPS: '))
    if Empregado['ctps'] > 0 :
        Empregado['aInicio'] = int(input('Qual o ano de inicio proficional: '))
        Empregado['salario'] = float(input('Qual o salario de :'))
        Empregado['Aposenta'] = Empregado['aInicio'] + 35
    Empregados.append(Empregado.copy())
    Continue = str(input('Desja continuar a cadastra [s/n] :'))
#Empregados = [{'nome': 'Carlos', 'anasc': 1970, 'idade': 53, 'ctps': 34122, 'aInicio': 1988, 'salario': 1500.0, 'Aposenta': 2023}, {'nome': 'Jacira', 'anasc': 1976, 'idade': 47, 'ctps': 25, 'aInicio': 1995, 'salario': 2500.0, 'Aposenta': 2030}, {'nome': 'Margot', 'anasc': 1985, 'idade': 38, 'ctps': 0, 'aInicio': 1995, 'salario': 2500.0, 'Aposenta': 2030}, {'nome': 'Marculina', 'anasc': 1964, 'idade': 59, 'ctps': 263, 'aInicio': 1980, 'salario': 1200.0, 'Aposenta': 2015}]
print(Empregados)
for emp in Empregados :
    if emp['ctps'] == 0 :
        print(f'Trabalhador {emp["nome"]} nascido em {emp["anasc"]} Idade de {emp["idade"]} não possui carteira de trabalho.\n\n')
    else:
        print(f'Trabalhador {emp["nome"]} nascido em {emp["anasc"]} Idade de {emp["idade"]} possui carteira de trabalho nº {emp["ctps"]}.')
        print(f'Se aposenta em {emp["Aposenta"]} seu salario e de R${emp["salario"]:.2f}. \n\n')
    