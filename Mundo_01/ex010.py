#!/bin/python3

# ler quantos reais tem na carteira e mostre quantos dolares pode comprar.
# Considerar dolar 3,27

n1 = float(input('Digite o valor encontrado em sua carteira:'))

print('Os R$ {} encontrados em sua carteira podem ser convertidos em US$ {:.4f} \ncom base no cambio que e de US$ 3,27'.format(n1,(n1/3.27)))

