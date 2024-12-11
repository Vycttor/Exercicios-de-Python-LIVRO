'''
Ex.5.1 Modifique o programa para exibir os números de 1 a 100.
'''
#Código feito dia 14/11/2024

from time import sleep

cont = 1 # Variavel contador

while cont <= 100:
    sleep(1)
    print(cont)
    #print(cont, end =' ')
    cont += 1

