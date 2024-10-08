from os import system

system('clear')

frase = str(input('Digite o nome completo: ')).strip()
print('Texto Normal:                ' + frase)
print('Em Maiusculas                ' + frase.upper())
print('Em Minusculas                ' + frase.lower())
print('Comprimeto total Tamanho     ' + str(len(frase)))
print('Quantidade de Espaços        ' + str(frase.count(' ')))
print('Tamanho sem espaços          ' + str(len(frase) - frase.count(' ')))
print('Tamanho da 1º palavra        ' + str(len(frase.split()[0])))