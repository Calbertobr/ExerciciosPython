#!/bin/python3
import os
os.system('clear') or None

# Programa que converte temperatura em Celsius pra Fahrenheit.


temp = float(input('Quan valor de temperatura em graus Celcius a ser convertido :'))

print('A temperatua de {} °C e equivalente a {} °F '.format(temp,(temp*9/5+32)))