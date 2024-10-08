#!/bin/python

from os import system
system('clear')

Continua = 'S'

ContPessoas = 0
Maiores18 = 0
Homens = 0
Mulheres20 = 0
while Continua == 'S':
    Idade = 0
    Sexo = ''
    print('-'*20)
    while Sexo != 'M' and Sexo != 'F':
        Sexo = str(input('Escolha o Sexo [F/M]:')).strip().upper()[0]
    while Idade <= 0 :
        Idade = int(input('Digite a idade :'))
    
    ContPessoas +=  1
    if Idade > 18 :
        Maiores18 += 1
    if Sexo == 'M' :
        Homens += 1
    if Idade < 20 and Sexo == 'F' :
        Mulheres20 += 1

    Continua = str(input('Deseja continuar [S/N]')).strip().upper()[0]


print(f"""
    Total de pessoa(s) {ContPessoas}
    Pessoa maiores de 18 anos temo(s) {Maiores18}.
    Ao todo temos {Homens} home(s) cadastrado(s).
    E temos {Mulheres20} mulher(es) com menos de 20 anos
""")


