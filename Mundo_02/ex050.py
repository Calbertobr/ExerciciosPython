# Solicitar 6 numeros e somar os pares 
from os import system
system('clear')
SomaPar = 0
SomaImp = 0
for a in range(0,6):
    num = float(input('Digite o {}º numero: '.format(a+1)))
    if num % 2 == 0:
        SomaPar += num
    else:
        SomaImp += num
print('A soma dos pares e igual a {}'.format(SomaPar))
print('A soma dos impares e igual a {}.'.format(SomaImp))