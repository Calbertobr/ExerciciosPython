#!/bin/python

from os import system
system('clear')

Classifc = ('Botafogo','Palmeiras','Grêmio','Fluminense','Cruzeiro','Atlético-MG','Flamengo',\
            'Fortaleza','Athletico-PR','São Paulo','Santos','Goiás','Bragantino','Cuiabá','Bahia',\
            'Internacional','Vasco','Corinthians','América-MG','Coritiba')

print(f'A - Primeiros cinco colocados:\n{Classifc[:5]}\n')
print ('A - Primeiros cinco colocados: ')
for a in Classifc[:5] :
    print(f' {a}',end='')
print('\n'+'--'*20)
print(f'\nB - Os Quatro ultimos Zona de Rebaixamento:\n{Classifc[-4:]}\n')
print ('B - Os Quatro ultimos Zona de Rebaixamento:')
for a in Classifc[-4:] :
    print(f' {a}',end='')
print('\n'+'--'*20)
print(f'\nC - Todos em ordem alfabetica:\n{sorted(Classifc)}\n')
print ('C - Todos em ordem alfabetica:')
for a in sorted(Classifc) :
    print(f' {a}',end='')
print('\n'+'--'*20)
print('D - Em que posição esta o time do Bragantino: ')

for id, nome in enumerate(Classifc) :
    if nome == 'Bragantino' :
        print(f'O bragantino esta na classificação {id+1}, porem na lista e o numero {id}.')

