# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e preço a pagar.

def desconto(a,b): # a = valor da mercadoria b = valor do percentual de desconto.
    valordescont = (b*a)/100 #Calculo valor de desconto
    print ("O valor de desconto é de R$ {:.2f} reias ".format(valordescont))
    print("\n")
    precodesconto = a - valordescont #Calculo do desconto, preço mercadoria com desconto.
    print("O preço da mercadoria de R$ {:.2f} reais, com desconto de R$ {:.2f} reais ".format(a,valordescont))
    print("Passa a custar R$ {:.2f} reais ".format(precodesconto))

print("PROGRAMA CALCULA O VALOR DE DESCONTO SOBRE O VALOR DE UMA MERCADORIA\n")
a = float(input("Digite o valor da mercadoria: "))
b = float(input("Digite o valor de desconto: "))
print("\n")

#Chama/invoca a função desconto(a,b):
desconto(a,b)