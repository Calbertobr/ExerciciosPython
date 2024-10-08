# Soma de numeros multiplos de 3 entre 1 e 500
from os import system
system('clear')

Soma = 0
for a in range(1,501,2):
    if a%3 == 0 :
        print(' {}'.format(a),end='')
        Soma += a
print('')
print('A soma dos numero divisiveis por 3 entre 1 e 500 e {}'.format(Soma))


