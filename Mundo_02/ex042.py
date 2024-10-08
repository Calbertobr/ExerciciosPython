from os import system
system('clear')
Lado=[]
for l in range(0,3):
    Lado.append( float(input('Digite o {}º lado do triangulo: '.format(l+1))))
Lado.sort()
if ( Lado[0] + Lado[1] )  > Lado[2] :
    if Lado[0] == Lado[1] == Lado[2] :
        print('Este e um triangulo Equilatero.') 
    elif Lado[0] == Lado[1] or Lado[1] == Lado[2] :
        print('Este e um triangulo Isoceles.')
    else:
        print('Este e um triangulo Escaleno')
else:
    print('As tres medidas não formam um triangulo.')

    