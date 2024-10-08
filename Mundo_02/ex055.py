# Entre com peso de 5 pessoas e identifique qual menor peso e maior peso.
from os import system
from datetime import datetime
system('clear')
Maior = 0
Menor = 999
for a in range(0,5):
    Peso = float(input('Digite o peso da {}ª Pessoa: '.format(a+1)))
    if Peso > Maior :
        Maior = Peso
    if Peso < Menor :
        Menor = Peso

print('O pessoa mais leve tem {}Kg e a mais pesada tem {}Kg.'.format(Menor,Maior))
