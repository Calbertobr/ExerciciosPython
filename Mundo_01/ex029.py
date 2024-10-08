from os import system
system('clear')

Veloc = float(input('Qual a velocidade atual: '))

if Veloc > 80:
    print('Voce ultrapassou a velocidade de 80Km de Limite.')
    print('Sua multa e de {:.2f} Reais'.format((Veloc-80)*7))
else:
    print('Continue sua Viagem:')
    