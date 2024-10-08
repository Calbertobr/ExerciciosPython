from os import system
system('clear')


# 0 None
# 1 Bold
# 4 Undescore
# 7 Negative

# 30 Branco       40 Background
# 31 Vermelho
# 32 Verde
# 33 Amarelo
# 34 Azul
# 35 Lilaz
# 36 Ciano
# 37 Cinza

print('\33[0;30;41m Ola Mundo!\33[m')

print('{:=^40}'.format('\33[0;30;41mB A R R I G A\33[m'))