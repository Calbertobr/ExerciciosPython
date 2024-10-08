#!/bin/python3

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

print('Os resultados aritimeticos entre os numeros {} e {} são:'.format(n1,n2))
print('='*50)
print('Soma:                  {:>30.3f} '.format((n1+n2)))
print('Subtração:             {:>30.3f} '.format((n1-n2)))
print('Multiplicação:         {:>30.3f} '.format((n1*n2)))
print('Divisão:               {:>30.3f} '.format((n1/n2)))
print('Exponencial:           {:>30.3f} '.format((n1**n2)))
print('Divisão Int Quociente: {:>30.3f} '.format((n1//n2)))
print('Divisão Int Resto:     {:>30.3f} '.format((n1%n2)))
print('Raiz Quadrada      1°: {:>30.3f}     2°: {:>10.3f}'.format((n1**(1/2)),(n2**(1/2))))
print('Raiz Cubica        1°: {:>30.3f}     2°: {:>10.3f}'.format((n1**(1/3)),(n2**(1/3))))

print('Buceta',end=' ')
print('Cabeluda')

