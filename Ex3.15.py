#Ex 3.15 Escreva um programa para calcular a redução do tempo de vida de um fumante.
#Pergunde a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
#Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias
#de vida um fumante perderá. Exiba o total em dias.

def dias_de_vida_perdido(q_cigarros,anos):

    #Variáveis locais para função
    perda_de_vida = 10 # Minutos perdidos por cigarro fumado.
    hora = 60 # Hora
    dia = 24 # Dia

    #Calculo de tempo de vida perdido, por cigarro fumado.
    tempo_perdido = q_cigarros*perda_de_vida
    print("O total de tempo perdido é de {:.2f} minutos ".format(tempo_perdido))
    print("\n")

    #Calculo de conversão dos minutos em horas.
    minutos_para_horas = tempo_perdido / hora
    print("{} minutos, convertido equivale a {:.2f} horas ".format(tempo_perdido,minutos_para_horas))
    print("\n")
    
    #Calculo de conversão do tempo de horas para dias.
    dias_de_vida_perdidos =  minutos_para_horas / dia
    #print("O Fumante perdeu {:.0f} dias de vida ".format(dias_de_vida_perdidos))
    #print("\n")

    #Calculo total de tempo de vida perdido pelo usuario.
    total_tempo_perdido = dias_de_vida_perdidos*anos
    print("O total de tempo de vida perdido pelo usuario é de {:.0f} dias ".format(total_tempo_perdido))
    print("\n")

print("PROGRAMA INFORMA QUANTOS DIAS DE VIDA FOI PERDIDO COM O CONSUMO DE CIGARRO\n")  
# Linha abaixo solicita para o usuario digitar as informações solicitadas.
q_cigarros = int(input("Informe a quantidade de cigarros fumados por ano: "))
anos = int(input("Informe a quantidade de anos que o usuario ja fumou: "))
print("\n")

#Chama/invoca a fução que calcula os dias de vida perdido.
dias_de_vida_perdido(q_cigarros,anos)