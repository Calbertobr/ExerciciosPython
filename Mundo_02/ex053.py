# Verificar se uma frase e um palindromo
from os import system
system('clear')

#frase = str(input('Gigite uma frase: ')).strip().replace(' ','')
#ou
frase = str(input('Gigite uma frase: ')).strip()
palavra = frase.split()
frase = ''.join(palavra)
Ifrase = ''
for a in range(len(frase),0,-1) :
    Ifrase += frase[a-1] 
if frase == Ifrase :
    print('A frase e um palindromo.')
else:
    print('esta frase não e um palindromo.')
print(' {} <> {} '.format(frase, Ifrase))