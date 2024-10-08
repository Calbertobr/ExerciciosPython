

from os import system
system('clear')


def leia(tipo):
    while True:
        try:
            if tipo == 'int':
                value = int(input('Divite um numero inteiro: '))
            elif tipo == 'float':
                value = float(input('Digite um numero real: '))
            elif tipo == 'str':
                value = str(input('Digite uma string: '))
            elif tipo == 'menu':
                value = int(input('Digite uma das opções acima: '))
            else :
                print('\033[31m Error não foi selecionado o tipo de valor! \033[m ')
        except:
            system('clear')
            print('\033[31m Valor digitado não condiz com o solicitado.\033[m')
            continue
        else:
            return value
        
def Menu(Data):
    print(30*'_')
    for lista in Data :
        print(f" { lista[0]} - {lista[1]}")
    print(30*'_')