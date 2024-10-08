#!/bin/python

import os
import math

os.system('clear')

num = float(input('Digite um numero real : '))

print('1 - Os valores são Inteiro {} decimal {} '.format(num,math.trunc(num)))

print('2 - Os valores são Inteiro {} decimal {} '.format(num,int(num)))

