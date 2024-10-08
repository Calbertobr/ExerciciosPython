# Verificar se um numero e primo
from os import system
system('clear')
num = int(input('Digite o numero para ver se ele e primo: '))
Verdade = 0
for a in range(1,num+1):
    if num % a == 0 :
        print(' \033[34m{}\033[m'.format(a),end='')
        
        if a > 1 and a < num :
            Verdade += 1
        elif a < num:
            Verdade += 0
    else:
        print(' \033[31m{}\033[m'.format(a),end='')
        Verdade += 0
if Verdade == 0 :
    print('\n{} e um numero primo.'.format(num))
else:
    print('\n{} não e um numero primo.'.format(num))
    print('Ele e divisivel por outro numero que não seja 1 ou ele mesmo.')         

        