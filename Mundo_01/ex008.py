#!/bin/python3

# Ler um valor em metros e converter em centimetros e milimetros 

n1 = float(input('Digite u valor em metros a ser convertido:'))

print('Em KM {:>12}\nEm hm {:>11}\nEm dam {:>9}\nEm m  {:>10}\nEm dm {:>10}\nEm cm {:>10}\nEm mm {:>10}\n'.format ((n1/1000),(n1/100),(n1/10),n1,(n1*10),(n1*100),(n1*1000)))