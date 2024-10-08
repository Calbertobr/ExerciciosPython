from os import system
system('clear')

nomecompleto = input('Digite o nome completo: ')

nomes = nomecompleto.split()

print('O primeiro nome e {} e o ultimo e {}'.format(nomes[0],nomes[len(nomes)-1]))
