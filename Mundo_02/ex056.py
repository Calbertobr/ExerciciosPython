# Leia nome, idade, sexo de 4 pessoas e diga #   - media de idade #   - Nome do homem mais velho#   - Quantas mulheres menores de 20
from os import system
system('clear')
Data = {}
SomaIdate = 0
Nome = ''
Qtd = 0
MaisVelho = 0
for a in range(0,4):
    nome  = str(input('Qual seu nome: '))
    idade = int(input('Qual a sua idade: '))
    Sexo  = int(input('Qual sexo:  [ 1 ]  Masculino [ 2 ] Feminino: '))
    SomaIdate += idade 
    if Sexo == 1 and idade > MaisVelho  :
        MaisVelho = idade
        Nome = nome
    if Sexo == 2 and idade < 20 :
        Qtd += 1 
    Data[a] = [nome,idade,Sexo]
print(Data)
print('A media de idade dos relacionados e de {}.'.format(SomaIdate/4))
print('O homem mais velho e o {}'.format(Nome))
print('Temos {} mulhere(s) com idade inferior a 20 anos.'.format(Qtd))
