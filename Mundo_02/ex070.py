#!/bin/python
from os import system
system('clear')
Continua = 'S'
Soma = 0
Caros = 0
ValorMenor = 9999999999999999
ValorProd = 0
NomeBarato = ''
while Continua == 'S' :
    Nome = str(input('Qual nome do produto: ')).strip()
    ValorProd = float(input('Qual o valor do produto: '))
    if ValorMenor > ValorProd:
        NomeBarato = Nome
    if ValorProd > 999 :
        Caros +=1
    Soma += ValorProd
    Continua = str(input('Continua [S/N]? ')).upper().strip()[0]
print(f"""
    O total de gastos com a compra foi de R$ {Soma:.2f}.
    Foram encontrados {Caros} Produtos custando mais de R$ 1000,00.
    Ja o produto mais barato foi o {NomeBarato}.
""")