from os import system
from datetime import date
system('clear')

ano = int(input('Digite o ano em consulta ou 0 para ano atual: '))

if ano == 0 :
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0 :
    print('O ano {} e bisexto'.format(ano))
else:
    print('O ano {} e normal.'.format(ano))