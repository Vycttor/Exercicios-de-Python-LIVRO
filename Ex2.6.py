#2.6 Modifique o Programa 2.2, de forma que ele calcule um almento de 15% para um salario de R$ 750

#Variáveis globais
b = 15

# Função para o calculo de porcentagem
def porcet(a,b):
    aument15 = (b*a)/100
    print ("O aumento de 15% é de: ",aument15)
    aumentfinal = a + aument15
    print ("O aumento de 15%, de: ",a,"é =: ",aumentfinal)



print ("Programa calcula o aumento de 15 por cento de um valor\n")
a = float(input("Digitar o valor para calculo do aumento de 15%: "))

#Função chama/invoca o calculo
porcet (a,b)

