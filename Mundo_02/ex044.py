#Calcular o valor do produto de acordo com o mode de pagamento.
from os import system
system('clear')

Valor = float(input('Qual o Valor do produto: '))
Meio  = int(input('''Escolha a opção de pagamento:\n- 1 A vista Dinheiro ou Cheque:\n- 2 A vista no Cartão:\n- 3 Em duas Vezes no Cartão:\n- 4 Em 3x ou mais no cartão:\n'''))

if Meio == 1 :
    print('O valor e de R$ {}.'.format(Valor*.9))
elif Meio == 2 :
    print('O valor e de R$ {}.'.format(Valor*.95))
elif Meio == 3:
    print('O valor e de R$ {}.'.format(Valor))
elif Meio == 4:
    print('O valor e de R$ {}.'.format(Valor*1.2))
else:
    print('Escolha errada de opção')
    