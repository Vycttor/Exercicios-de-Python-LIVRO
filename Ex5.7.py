'''
Ex 5.7 Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
'''
t = int(input('Tabuada:'))
i = int(input('Informe o inicio da tabuada:'))
f = int(input('Informe o fim da tabuada: ')) 


while i <= f:
    print(f'{t} X {i} = {i*t}')
    i += 1