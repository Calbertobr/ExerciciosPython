# Dar entrada no ano de se pessoas e verificar quais são maiores de idade.
from os import system
from datetime import datetime
system('clear')

ContM = 0
Contm = 0

for a in range(0,7):
    ano = int(input('Qual seu ano de nascimento: '))
    if datetime.today().year - ano >= 21 :
        ContM += 1
    else:
        Contm += 1
print('Temos {} pessoas maiores de idade.'.format(ContM))
print('Temos {} pessoas menores de idade.'.format(Contm))
