from os import system
system('clear')

print(' - '*40)
print('Financiamento.')

Salario = float(input('Informe seu salario: '))
Imovel = float(input('Informe o valor do imovel a financiar: '))
Periodo = int(input('Em quantos anos projeta pagar o financiamento: '))
Entrada = float(input('Qual o valor da entrada: '))
ParcelaMax = ( Salario * .30 )
ValorParcela = (( Imovel - Entrada ) / ( Periodo * 12 ) )


print('O valor disponivel de seu salario para financiamento e de R$  {:.2f}.\n'.format(ParcelaMax))
print('Considerando a entrada de R$ {:.2f} O saldo de {:.2f}.\n'.format(Entrada,Imovel-Entrada))
print('Com a quantidade de {} parcelas as prestações terão o Valor de R$ {:.2f}.\n'.format(Periodo*12,ValorParcela))

if ValorParcela >= ParcelaMax :
    print('Como o valor da pacela e acima do permitido o financiamento não foi liberado.\n')
else:
    print('Parabens, Seu financiamento foi liberado !!!!\n')





