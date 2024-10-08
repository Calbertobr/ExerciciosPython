#!/bin/python
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

import utilidade.dado as dado
import utilidade.moeda as moeda
from os import system
system('clear')

preco = dado.leiadineiro('Valor a ser analisado: ')
system('clear')
moeda.resumo(preco,80,50)