from os import system
from random import shuffle
system('clear')

frase = '  Comprei um carro velho que so da despesa, uma bomba !!!  '

print (frase)

print(len(frase))
print(frase.count('a'))
print(frase.strip())
print(frase.split()[1])
print(frase.lower())
print(frase[:13])
labo = frase.strip()

t1 = labo[0::3]
t2 = labo[1::3]
t3 = labo[2::3]
print('#'+t1+'#  '+str(len(t1)))
print('#'+t2+'#  '+str(len(t2)))
print('#'+t3+'#  '+str(len(t3)))

corr = ''
qt = int(len(frase)/3)+1

for a in range(0,qt):
    print(corr)
    if a < len(t1):
        corr = corr + str(t1[a])
    if a < len(t2):
        corr = corr + str(t2[a])
    if a < len(t3):
        corr = corr + str(t3[a])
print('-----------------------------------------')    
print('-'.join(frase.split()))

