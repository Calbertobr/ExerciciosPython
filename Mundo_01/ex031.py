
from os import system
system('clear')

percurso = float(input('Quantos kilometros te a viagem: '))

if percurso <= 200 :
    Valor = percurso*.5
else:
    Valor = percurso*.45

print('Esta viagem vai custar {:.2f} Reais.'.format(Valor))