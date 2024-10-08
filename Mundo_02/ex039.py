# Calcular com base em uma data se esta dentro do periodo de alistamento militar
# Inicia se no ano em que completar 18 e termina no mes de juho
from os import system
import datetime
system('clear')

Data = str(input('Qual sua data de nascimento DD/MM/YYYY: ')).split('/') 
NiverNext = datetime.date( int(Data[2])+18 , int(Data[1]) , int(Data[0]))
Niver = datetime.date( int(Data[2]) , int(Data[1]) , int(Data[0]))
Agora = datetime.date.today()
# Teste@ Agora = datetime.date(2023,7,2)

Idade = Agora - Niver
Limite = datetime.date(datetime.date.today().year,12,31)
print('Sua idade e de {} anos'.format(Idade.days//365))
if NiverNext >= datetime.date(Agora.year,1,1) and NiverNext <= datetime.date(Agora.year,12,31) :
    if Agora > datetime.date(Agora.year,6,30) :
        print('\033[0;0;31mVoce esta em periodo de alistamento militar, porem perdeu a data que foi ate 30/06/{}.\033[m'.format(Agora.year))
    else:
        print('Voce esta em periodo de alistamento militar\nCompareca a junta militar ate 30/06/{}.'.format(Agora.year))
elif NiverNext > datetime.date(Agora.year,12,31) :
    print('Voce não tem idade suficiente para se alistar, Falta {} Anos.'.format(NiverNext.year - Agora.year))
else:
    print('\033[0;0;31mVoce perdeu o prazo de alistamento militar a {} anos.\033[m'.format( Agora.year - NiverNext.year))


