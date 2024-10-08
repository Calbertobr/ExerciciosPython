
from math import radians,tan, sin ,cos
import os
os.system('clear')

angulo = radians(float(input('Digite o cangulo: ')))


tang = tan(angulo)
seno = sin(angulo)
cose = cos(angulo)

print('O angulo tem valores trigronometricos de:\nTangente  {:>10.4f}\nSeno  {:>14.4f}\nCosseno  {:>11.4f}\n'.format(tang,seno,cose))