'''
Ex 5.9. Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20/4=5, uma vez que podemos subtrair 4 cinco vezes de 20.
'''

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))


cont = 0

while numero_1 >= 0:
    numero_1 -= numero_2
    cont += 1

resultado = cont -1
print(resultado) # Apenas imprime a divisão inteira




