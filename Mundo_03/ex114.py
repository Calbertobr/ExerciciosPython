#!/bin/python

import urllib, urllib.request
from os import system

system('clear')

try:
    site = urllib.request.urlopen('http://svr.weganne.com.br')
except:
    print('Site fora do ar:')
else:
    print('Site Ok.')
