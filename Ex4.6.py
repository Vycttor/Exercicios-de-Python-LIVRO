'''
Ex. 4.6  Escreva um programa que pergunte a ditância que um passageiro deseja percorrer em Km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
'''
#Código feito dia 09/11/2024.


print('=='*25)
distancia = float(input('Informe a distância da da viagem: km '))
print('=='*25)

#Condição verifica forma de cobrança que será aplicada
if distancia <= 200:
    preco_viagem = distancia*0.50
    print(f'{distancia:.0f} Km distância, O valor da sua viagem é de R$ {preco_viagem:.2f} reais')
    print('=='*25)
elif distancia > 200:
    preco_viagem = distancia*0.45
    print(f'{distancia:.2f} distância, O valor da sua viagem é de R$ {preco_viagem:.2f} reias')
    print('=='*25)
else:
    print('Erro valor digiato, tente novamente')
    print('=='*25)
