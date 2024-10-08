#!/bin/python

from os import system
system('clear')

Lista = ('Maça',5.19,'Morango',6.18,'Manga',12.5,'Jaca',16.4,'Banana',9.20,'Uva',16)
print('-'*30)
print(f'{"Lista de preços":^30}')
print('-'*30)
for a in range(0,len(Lista)//2,2) :
    print(f'   {Lista[a]:.<15} R$ {Lista[a+1]:5.2f}')