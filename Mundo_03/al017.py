
#!/bin/python

from os import system
system('clear')


# Cria lista
Lista = [3,5,6,9,1,8,9,15,16,7,18,92]
print(Lista)

# Adiciona valor 12 na ultima posição
Lista.append(12)
print(Lista)

# Insere 99 na posição 3
Lista.insert(3,99)
print(Lista)

# deleta Valor da posição 0
del Lista[0]
print(Lista)

# Exclui valor da posição 3
Lista.pop(3)
print(Lista)

#Remove o valor 8 da lista, Da erro se não existir.
Lista.remove(8)
print(Lista)
#Correto
if 99 in Lista:
    Lista.remove(99)
print(Lista)

# remove ultimo valor da lista
Lista.pop()
print(Lista)

# Ordenando lista
Lista.sort()
print(Lista)
Lista.sort(reverse=True)
print(Lista)

#Tamanho
print(len(Lista))

# Copia e espelho de lista
# Ligação
A = [2,3,6,4]
B = A

print(f'Lista A {A}')
print(f'Lista B {B}')
B[2] = 7 

print(f'Lista A {A}')
print(f'Lista B {B}')

# Copia
B = A[:]
A[2] = 9
print(f'Lista A {A}')
print(f'Lista B {B}')
