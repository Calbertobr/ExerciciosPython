from os import system
system('clear')

lista =[]

for a in range(0,3):
    data = (input('Digite o numero {} : '.format(a+1)))
    lista.append(data)

regs = len(lista)
lista.sort()
print(lista)
print('O numero menor e: {}'.format(lista[0]))
print('O numero maior e: {}'.format(lista[regs-1]))