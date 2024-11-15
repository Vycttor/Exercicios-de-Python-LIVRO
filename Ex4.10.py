'''
Ex 4.10.  Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

                               Preço por tipo e faixa de consumo

                               Tipo       Faixa(kWh)    Preço
                               Residência Até 500       R$ 0,40
                                          Acima de 500  R$ 0,65 

                               Comercial  Até 1000      R$ 0,55
                                          Acima de 1000 R$ 0,60

                               Indústrial Até 5000      R$ 0,55 
                                          Acima de 5000 R$ 0,60                    
'''
#Código feito dia 12/11/2024.

print('==='*25)
kwh = float(input('Informe a quantidade de kWh consumido: '))

#Menu para o usuario informar qual tipo de instalação é utilizada.
print('''
    [1] Residêncial
    [2] Comercial
    [3] Indústrial''')
tipo = int(input('Informe o tipo de instalação: '))
print('==='*25)


#Condição realiza calculo da cobrança de enegia eletrica.
if tipo == 1:
    if kwh <= 500:
        preco_conta_de_energia = kwh*0.40
        print(f'Tipo de instalação [{tipo}] Residência')
        print(f'O valor da conta de energia R$ {preco_conta_de_energia:.2f} reais')
    elif tipo > 500:
        preco_conta_de_energia = kwh*0.65
        print(f'Tipo de instalação [{tipo}] Residência')
        print(f'O valor da conta de energia R$ {preco_conta_de_energia:.2f} reais')
elif tipo == 2:
    if kwh <= 1000: 
        preco_conta_de_energia = kwh*0.55
        print(f'Tipo de instalação [{tipo}] Residência')
        print(f'O valor da conta de energia R$ {preco_conta_de_energia:.2f} reais')
    elif kwh > 1000:
        preco_conta_de_energia = kwh*0.60
        print(f'Tipo de instalação [{tipo}] Residência')
        print(f'O valor da conta de energia R$ {preco_conta_de_energia:.2f} reais')
elif tipo == 3:
    if kwh <= 5000:
        preco_conta_de_energia = kwh*0.55
        print(f'Tipo de instalação [{tipo}] Residência')
        print(f'O valor da conta de energia R$ {preco_conta_de_energia:.2f} reais')
    elif kwh > 5000:
        preco_conta_de_energia = kwh*0.60
        print(f'Tipo de instalação [{tipo}] Residência')
        print(f'O valor da conta de energia R$ {preco_conta_de_energia:.2f} reais')
print('==='*25)