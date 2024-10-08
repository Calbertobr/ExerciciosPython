# Mostrar dez termos de uma pa dados primeiro termo e a razao
from os import system
system('clear')

Ptermo = int(input('Digite o primeiro termo da pa: '))
Razao  = int(input('Digite o valor da razao da pa: '))
Next = Ptermo
print('Os termos são: ', end='')
for a in range(0,10):
    print(' {}'.format(Next), end='')
    Next +=Razao
print('\nFim')
print('='*10)
print('Os termos são: ', end='')
for a in range(Ptermo,( Razao * 10 + Ptermo ),Razao):
    print(' {}'.format(a), end='')
print('\nFim')
