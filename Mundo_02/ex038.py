from os import system
system('clear')

num1 = float(input('Digite um valor numerico: '))
num2 = float(input('Digite um segundo Valor numerico: '))

if num1 == num2 :
    print('Os {} e {} numeros são Iguais'.format(num1,num2))
elif num1 > num2 :
    print('O numero {} e maior que o numero {}.'.format(num1,num2))
else:
    print('O numero {} e menor que o numero {}.'.format(num1,num2))

