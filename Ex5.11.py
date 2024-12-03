'''
Ex. Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
'''
cont = 1
soma = 0
somaj = 0
mes = 1

deposito = float(input('Informe o valor de depósito:R$ '))
juros_poupanca = float(input('Informe o taxa de juros:% '))

while cont <= 10: 

    soma = soma + deposito

    #somaj = soma + (soma*juros_poupanca) / 100
    print(f'[{mes}]: R$ {soma:.2f}')
    cont = cont + 1
    mes = mes + 1
   

print(f'Soma dos 24 meses {soma}')

#pendente calcular juros mes a mes

    