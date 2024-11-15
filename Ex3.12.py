#Escreva um programa que calcule o tempo de uma viagem  de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

#Função, realiza o carculo de tempo da viagem
def tempoviagem(n1,n2):
    mediavelocidade = n1/n2
    print("O tempo estimado para a viagem é de: {:.2f} horas".format(mediavelocidade))
    print("\n")

print("PROGRAMA CALCULA VELOCIDADE MÉDIA ESPERADA PARA UMA VIAGEM\n")
n1 = float(input("Digite a distância da viagem: "))
n2 = float(input("Didite a velocidade média esperada: "))
print("\n")
#Chama invoca a função, que calcula o tempo da viagem
tempoviagem(n1,n2)