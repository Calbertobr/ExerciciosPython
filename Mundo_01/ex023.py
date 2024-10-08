from os import system

system('clear')

num = int(input('Digite um numero: '))
un = num // 1 % 10
de = num // 10 % 10
ce = num // 100 % 10 
mi = num // 1000 % 10

print('Milhar    {}'.format(mi))
print('Centena   {}'.format(ce))
print('Dezena    {}'.format(de))
print('Unidade   {}'.format(un))
print('----------------- int ----------------------')

