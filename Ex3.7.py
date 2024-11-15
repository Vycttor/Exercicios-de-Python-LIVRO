#3.7 Faça um programa que peça dois numeros inteiros. Imprima a soma desses dois numeros na tela.



#Função de soma de valores.
def soma(a,b):
    c = a+b
    print ("A soma é = ",c)

print ("PROGRAMA REALIZA A SOMA DE DOIS VALORES INTEIROS\n")
# Pede para o usuario didigitar dois valores.
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
print("\n")
#Chama/invoca a função soma.
soma(a,b)