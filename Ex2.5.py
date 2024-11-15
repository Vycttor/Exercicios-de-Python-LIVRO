#2.5 Escreva um programa que calcule a soma de três variaveis e imprima o resultado na tela.

#Foi criado abaixo uma função para realizar a soma das três variáveis
def soma(a,b,c):
    soma = a+b+c
    print ("A soma das três variáveis é =: ", soma)

print (" Programa apresenta na tela a soma de três variáveis")
#Silicita para o usurio o valor das variáveis
a = int(input("Digite o valor da primeira variável: "))
b = int(input("Digite o valor da segunda variável: "))
c = int(input("Digite o valor da terceira variável: "))

# Invova/ chama a Funcão para realizar o calculo e mostrar na tela.
soma(a,b,c)
