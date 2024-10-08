from os import system
system('clear')

sal = float(input('Qual o salario a ser corrigido: '))

if sal <= 1250:
    saln = sal*1.15
else:
    saln = sal*1.1

print('O seu salario de R$ {:.2f} passa a ser de R$ {:.2f}'.format(sal,saln))

