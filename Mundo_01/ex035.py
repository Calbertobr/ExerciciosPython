from os import system
system('clear')

lista = []

for a in range(0,3):
     lista.append(float(input('Digite o valor da {}ª aresta do triangulo: '.format(a+1))))

lista.sort()

if lista[0] + lista[1] > lista[2] :
     print('As tres retas forman um triangulo.')
else:
     print('As tres retas não forman um triangulo.')
