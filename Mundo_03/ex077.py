#!/bin/python

from os import system
system('clear')
Tupla = ('Amor','Felicidade','Casa','Cachorro','Gato','Computador','Livro','Coracao','Beleza','Sol','Chuva','Familia','Amigo','Comida','Trabalho','Escola','Musica','Praia','Sorriso','Esperanca')
for a in Tupla :
    print(f'Na palavra {a:16} temos vogais ',end='')
    for b in range(0,len(a)) :
        if a[b] in 'aeiouAEIOU' : 
            print(f' {a[b]}',end='')
    print(' .')