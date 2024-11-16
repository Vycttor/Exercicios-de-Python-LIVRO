'''
Ex. 5.4. Modifique o programa anterior (pg 87) para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.


'''
#Programa modificado na condição if, para apenas imprimir numeros impares.

fim = int(input('Digite o último número a imprimir: '))

cont = 0

while cont <= fim:
    if cont % 2 == 1: #Resto divisão 
        print(cont)
    cont += 1
