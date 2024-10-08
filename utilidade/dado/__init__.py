
def leiadinheiro(msg) :
    
    while True :
        data = input(msg).replace(',','.')
        if data.replace('.','').isnumeric():
            data = float(data)
            return data
        else:
            print('\033[0;33mNumero invalido:\033[m')


def leiaint(msg):
    while True :
        data = input(msg)
        try:
            data = int(data)
            print(f'Data correto {data}')
            break
        except:
            print(f'O valor digitado e invalido {type(data)}')

            



def leiafloat(msg):
    while True:
        data = input(msg).replace(',','.')
        try:
            data = float(data)
            print(f'Data Correto {data}')
            break
        except:
            print(f'Valor invalido {type(data)}') 