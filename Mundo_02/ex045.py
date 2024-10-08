# Jokenpô
from os import system
from random import randrange
system('clear')
JogadaCpu = randrange(0,2)
Opcoes = ['Pedra','Tesoura','Papel']
#print(Opcoes[JogadaCpu])

Jogada = int(input('Escolha sua jogada:\n1 Pedra.\n2 Tesoura.\n3 Papel.\n'))-1

print('O computador escolheu {} e voce escolheu {} portanto:'.format(Opcoes[JogadaCpu],Opcoes[Jogada]))

if Jogada == JogadaCpu :
    print('Deu empate entre você e o computador.')
elif JogadaCpu == 0 and Jogada == 1 or JogadaCpu == 1 and Jogada == 2 or JogadaCpu == 2 and Jogada == 0 :
    print('Computador venceu !!!!')
else:
    print('Jogador venceu !!!!')