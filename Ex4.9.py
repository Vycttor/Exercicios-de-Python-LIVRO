'''
Ex 4.9 Escreva um programa para aprovar um empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode  ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividindo pelo número de meses a pagar.
'''
#Código feito dia 12/11/2024.

print('==='*20)
valor_casa = float(input('Informe o valor da casa:R$ '))
salario = float(input('Informe seu salário:R$ '))
anos_para_pagar = int(input('Informe em quantos anos deseja pagar: '))
print('==='*20)

#calculo 30% do salário
salario_30 = (salario*0.30)
print(f'30% do Salário: R$ {salario_30:.2f} reais')

#Parcelas anual
parcela_anual = valor_casa / anos_para_pagar 
print(f'Parcelas anuais: R$ {parcela_anual:.2f} reais')

#Parcelas mensais
parcelas_mensais = parcela_anual / 12
print(f'Parcelas mensais: R$ {parcelas_mensais:.2f} reais')
print('==='*20)
print('\n')

if parcelas_mensais <= salario_30:
    print('Empréstimo APROVADO')
else:
    print('Empréstimo REPROVADO')
print('==='*20)