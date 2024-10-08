from os  import system
from random import shuffle
system('clear')


Lista =[]
for a in range(0,4):
    Lista.insert(a,input('Digite o nume do aluno: '))

shuffle(Lista)
print(Lista)


