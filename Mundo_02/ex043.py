# Calculo de imc e listar faixa que se enquadra

from os import system
system('clear')

Peso = float(input('Qual seu pesos em (Kg): '))
Altura = float(input('Qual sua altura (m): '))
Imc = Peso / Altura ** 2

print(Imc)

if Imc < 18.5:
    print('Abaixo do peso.')
elif Imc < 25:
    print('Peso Ideal.')
elif Imc < 30:
    print('Sobrpeso.')
elif Imc < 40:
    print('Obesidade.')
else:
    print('Peso Morbido.')
