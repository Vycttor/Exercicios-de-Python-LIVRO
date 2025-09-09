'''
Ex 5.8. Escreva um programa que leia dois numeros. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize operadores de soma e subtração para calcular o resultado. Lembre se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim , 4x5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
'''

print("===========================================")
numero_1 = int(input("Digite o primero número: "))
numero_2 = int(input("Digite o segundo número: "))
print("===========================================")
print()

cont = 1
resultado = 0

while cont <= numero_1:
    cont += 1
    resultado += numero_2
    


if numero_1 == numero_2:
    print(f"{numero_1}X{numero_2}={resultado}")
elif numero_1 > numero_2:
    print(f"{numero_1}X{numero_2}={resultado}")
else:
    print(f"{numero_1}X{numero_2}={resultado}")
    