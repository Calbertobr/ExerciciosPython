lanche = ('Buceta', 'Cu', 'Peitos', 'Gprofunda')

print(lanche[1])

for a in lanche :
    print(f'Eu vou comer {a} de mamae.')

for a in range(0,len(lanche)):
    print(f' {a} {lanche[a]}')

for i, a in enumerate(lanche) :
    print(f'{i} {a}')
#
# print(lanche[-2:])
#print(lanche[2:])
print('-'*20)
print(lanche)
print(sorted(lanche))


a = (6,4,9,1,5,4)
b = (1,6,8,3,4)

c = a + b 
print(c)

print(c.count(4))

print(c.index(1))

tuplad = sorted(c)
print(tuplad)

del(tuplad)
print(tuplad)
