def aumento(Valor,Percent,format=False):
    Valor = Valor + ( Valor * Percent / 100 )
    return moeda(Valor,format)


def desconto(Valor,Percent,format=False):
    Valor = Valor - ( Valor * Percent / 100 )
    return moeda(Valor,format)


def dobro(Valor,format=False):
    Valor += Valor
    return moeda(Valor,format)


def metade(Valor,format=False):
    Valor /= 2
    return moeda(Valor,format)


def resumo(Valor,AumP,DesP):
    line('RESUMO DE VALOR')
    print(f'Valor Analisado: {moeda(Valor,True):>20}')
    line()
    print(f'Dobro do preço:  {dobro(Valor,True):>20}')
    print(f'Metade do preço: {metade(Valor,True):>20}')
    print(f'Aumento de {AumP}%:  {aumento(Valor,AumP,True):>20}')
    print(f'Desconto de {DesP}%: {desconto(Valor,DesP,True):>20}')
    line()

def moeda(Valor,format=False):
    if format :
        return f'R$ {Valor:8.2f}'.replace('.',',')
    else:
        return Valor

def line(msg=''):
    if msg != '':
        print('-' * 37 )
        print(f'{msg:^37}')
        print('-' * 37 )
    else:
        print('-' * 37 )
