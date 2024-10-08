# Conversão de base Binario Octal Exadecimal
from os import system
system('clear')
Inte = {}
Frac = {}
def converte(Valor,Base):
    print('Valor {} em base {}'.format( Valor, Base))
    Hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    Conversao = ''
    while Valor+Base-1 >= Base :    
        Q = Valor // Base
        R = Valor % Base
        if Base == 16 and R > 9 :
            Conversao = Hex[R] + Conversao
        else:
            Conversao = str(R)+Conversao
        #print('Q {} R {} '.format(Q,R))
        Valor = Q
    print('O valor convertido de {} em base {} e igaul a: {}'.format(Num,Base,Conversao))
    if Base == 2 :
        print(bin(Num)[2:])
    elif Base == 8 :
        print(oct(Num)[2:])
    elif Base == 16 :
        print(hex(Num)[2:])
    #    input('Pausa.')

Num = int(input('Digite o numero para conversão de base: '))
tipo = int(input('Qual base deseja converter: \n1 para binario\n2 para octal\n3 para exadecimal\n'))
if tipo == 1:
    Base = 2
elif tipo == 2:
    Base = 8
elif tipo == 3:
    Base = 16
else:
    print('Valor invalido de base.')
    exit()
converte(Num,Base)


