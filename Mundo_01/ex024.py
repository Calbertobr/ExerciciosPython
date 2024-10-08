from os import system
system('clear')

Cidade = str(input('Digite nome da cidade: ')).strip()
print(Cidade[:5].upper() == 'SANTO')

if Cidade.upper().split()[0] == 'SANTO':
    print('Sim a cidade tem Santo no inicio do nome.')
else:
    print('A cidade não começa com o nome Santo')
