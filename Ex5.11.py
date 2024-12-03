'''
Ex. Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
'''
cont = 0
soma = somaj = 0
mes = 0
print('==='*20)
print('========== POUPANÇA ==========')
print('==='*20)

deposito = float(input('Informe o valor de depósito:R$ '))
juros_poupanca = float(input('Informe o taxa de juros:% '))
print('==='*20)
print('\n')

while cont < 24: 
    soma = soma + deposito
    mes = mes + 1
    cont = cont + 1
    print(f'[{mes}]: R$ {soma:.2f}')
    if soma > 0:
        juros = (soma*juros_poupanca) /100
        #print(f'JUROS {juros}')
        somaj = somaj + juros
        #print(f'SOMAJ {somaj}')
print('\n')
print('==='*20)       
print(f'Valor depósito 24 mêses: R$ {deposito:.2f} reais ')     
print(f'Valor de juros da poupança {juros_poupanca} %')
print(f'Valor juros dos 24 mêses é de R$ {somaj} reais')
print(f'Total de rendimento dos 24 meses R$ {soma+somaj}')
print('==='*20)

