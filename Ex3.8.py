#3.8 Escreva um programa que leia um valor em metros e o exiba convertido em milimetros.


#Variáveis globais.
n1 = 1000

#Função para cornversão de metros em milimetros.
def milimetro(a,n1):
    milim = a*n1
    print ("O valor {}, convertido em milimetros é = {} milimetros" .format(a,milim))

print ("PROGRAMA MOSTRA A CONVERÇÃO DE UM VALOR EM MILIMETROS\n")

#Solicita para o usuario digitar um valor para a conversão
a = int(input("Digite um valor em metros para conversão: "))
print("\n")

#Função chama/invoca conversão dovalor.
milimetro(a,n1)
print("\n")