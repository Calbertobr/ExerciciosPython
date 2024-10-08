#!/bin/python
#Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.
from os import system
system('clear')


Pessoas = {'nome':'Gustavo','sexo':'M','idade':22}

print(f'O {Pessoas["nome"]} tem {Pessoas["idade"]} anos e o sexo e {Pessoas["sexo"]}')

print(Pessoas.keys())
print(Pessoas.items())
print(Pessoas.values())