from os import system
system('clear')

Nota1 = float(input('Digite a primeira nota: '))
Nota2 = float(input('Digite a segunda nota: '))

Media = ( Nota1 + Nota2 ) / 2

if Media < 5 :
    print('Reprovado Media: {:.2f}'.format(Media))
elif Media < 7 :
    print('Recuperação Media: {:.2f}'.format(Media))
elif Media >=7 :
    print('Aprovado Media: {:.2f}'.format(Media))