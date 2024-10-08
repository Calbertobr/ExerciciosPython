from os import system
import datetime
system('clear')

Entra = str(input('Qual sua data de nascimento dd/mm/yyyy : ')).split('/')
DataNascimento = datetime.date( int(Entra[2]), int(Entra[1]), int(Entra[0]))
Idade = int(datetime.date.today().year - DataNascimento.year) 
if  Idade <= 9 :
    print('Você faz parte da equipe mirim.')
elif Idade <= 14 :
    print('Você Faz parte da equipe Infantil.')
elif Idade <= 19 :
    print('Você faz parte da equipe Junior.')
elif Idade <= 20 :
    print('Você faz parte da equipe Sênior.')
else:
    print('Você faz parte da equipe Master.' )
