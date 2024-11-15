# 3.9  Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuario. Calcule o total em segundos.

# Variáveis globais
n0 = 86.400  # Um dia é = 86.400 segundos
n1 = 3.600  # Uma hora é = 3.600 segundos
n2 = 60  # Um minuto é = 60 segundos

# Função de conversão de todos os valores em segundos.
def convertsegu(dias, horas, minutos, segundos):
    diasegundos = dias*n0
    print("{} dias convetidos em segundos é = {:.3f} segundos ".format(
        dias, diasegundos))
    print("\n")

    horassegundos = horas*n1 # Calculo/formula conversão de horas em segundos.
    print("{:.2f} horas convertidos em segundos é =: {:.3f} segundos".format(horas, horassegundos))
    print("\n")

    minutossegundos = minutos*n2
    print("{:.2f} minutos convertidos em segundos é =: {:.0f}".format(minutos,minutossegundos))
    print("\n")

    segundossegundos = segundos
    print("{} segundos convertidos em sendos é =: {:.0f}".format(segundos,segundossegundos))
    print("\n")

    totalemsegundos = diasegundos+horassegundos+minutossegundos+segundossegundos
    print("O valor de todos os valores convertidos em segundos é=: {:.3f} ".format(totalemsegundos))


print("PROGRAMA CONVERTE TODOS OS VALORES SOLICIADOS EM SEGUNDOS\n")
dias = int(input("Digite a quantidade de dias: "))
horas = float(input("Digite a quantidade de horas: "))
minutos = float(input("Digite a quantidade de minutos: "))
segundos = int(input(" Digie a quantidade de segundos: "))
print("\n")

# Função de que calcula a conversão para segundos.
convertsegu(dias, horas, minutos, segundos)
print("\n")
