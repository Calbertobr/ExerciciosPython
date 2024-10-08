#!/bin/python
#Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

from os import system
system('clear')

ListaA = []
ListaB = []
ListaC = []

ListaA.append('Carlos')
ListaA.append(53)
print(ListaA)
ListaC.append('Sophia')
ListaC.append(33)
print(ListaC)

ListaB.append(ListaA)
print(ListaB)
ListaB.append(ListaC)
print(ListaB)



