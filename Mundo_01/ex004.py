#!/bin/python3

lido = input('Digite algo:')

print('O texto digitado tem tipo primitivo {}:'.format(type(lido)))
print('O texto digitado contem espaço: {}'.format(lido.isspace()))
print('O texto digitado e numerico: {}'.format(lido.isnumeric()))
print('O texto digitado e alfabetico: {}'.format(lido.isalpha()) )
print('O texto digitado e alfanumerico: {}'.format(lido.isalnum()))
print('O texto esta em Maiusculas {}.'.format(lido.isupper()))
print('O texto esta em Minusculas {}.'.format(lido.islower()))
print('O texto esta capitalizado {}.'.format(lido.istitle()))