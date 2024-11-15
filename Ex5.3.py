'''
Ex 5.3 faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10,9,8,...10 e Fogo! na tela.
'''

#Código feito dia 14/11/2024

from time import sleep

#Variavel contadora.
cont = 10

while cont >= 0:
    sleep(1)
    print(cont)
    cont -= 1
    #cont = cont - 1
print('FOGO!')