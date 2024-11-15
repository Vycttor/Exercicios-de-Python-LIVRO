# Ex 4.1 Escreva um programa que pergunte uma velocidade do carro de um usuário. Caso ultrapasse 80 Km/h, exiba uma mensagrem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

#Programa feito dia 16/10/2024.

velocidade = float(input(" Informe a velocidade carro: km/h "))

#Valor das varaveis e calculo da multa de velocidade.
i = 80
valor_taxa_por_km = 5
multa = (velocidade-i)*valor_taxa_por_km

#Condição If verificar se o carro vei ser multado ou não.
if velocidade < i:
    print("Velcocidade {} Km/h, dentro do padrão ".format(velocidade))
if velocidade > i:
     print("Velcocidade {} Km/h, fora do permitido ".format(velocidade))
     print('Velocidade {} ultrapassada, a multa é de R$ {:.2f} Reais'.format(velocidade,multa))

