#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salario
# e a porcentagem do aumento. Exiba o valor do aumento e do novo salario.


# Função porcentagem aumento salario
def aumentsalario(n1,n2):
    aumento = (n1*n2)/100 #n1 = porcentagem n2 = valor salarsalário
    print("O valor do aumento de {:.2f} % é = R$ {:.2f} reais".format(n1,aumento))
    print("\n")

    novosalario = n2+aumento
    print("O aumento de R$ {:.2f} reais + salário R$ {:.2f} é = R$ {:.2f} reais".format(aumento,n2,novosalario))
    print("\n")

print("PROGRAMA CALCULA O AUMETNO DO SALARIO")
print("\n")

n1 = float(input("Forneça a porcetagem (%) de aumento do salário: "))
n2 = float(input("Informer o valor do salário: "))
print("\n")
#Função chama/invoca calculo do aumento.
aumentsalario(n1,n2)


