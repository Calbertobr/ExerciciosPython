#!/bin/python

import os
os.system('clear')

Dias = float(input('Por quantos dias e o Aluguel: '))
Klms = float(input('Quantos kilometros percorreu: '))

Total = Dias * 60 + Klms * 0.15 



print('\nPara {:>6.2f} Km  o Valor e de R$ {:>5.2f}'.format(Dias,(Dias*60)))
print('Para {:>6.2f} Dias o valor e de R$ {:>5.2f}'.format(Klms,(Klms*.15)))
print('Valor total a ser pago e de R$ {:>7.2f}'.format((Dias*60+Klms*.15)))