'''
Ex 4.8 Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma(+), subtraçõa (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
'''
#Código feito dia 09/11/2024


#Menu de opções para o usuario escolher qual opção deseja realizar.
print("==="*20)
print('''
      [1] SOMA.
      [2] SUBTRAÇÃO.
      [3] MULTIPLICAÇÃO.
      [4] DIVISÃO''')
opcao = int(input('Escolha a opção de que desejá realizar o calculo: Nº '))
print("==="*20)
print('\n')


#Condição realiza operações conforme opção escolhida.
if opcao == 1:
    print('INFORME OS VALORES PARA SOMA')
    print('\n')
    valor_1 = float(input('Informe o primeiro valor: Nº '))
    valor_2 = float(input('Informe o segundo valor: Nº '))
    
    #Fórmula
    soma = (valor_1+valor_2)

    print(f'A soma de, {valor_1:.2f} + {valor_2:.2f}: = {soma:.2f}') 
    print('\n')
elif opcao == 2:
    print('INFORME OS VALORES PARA SUBTRAÇÃO')
    print('\n')
    valor_1 = float(input('Informe o primeiro valor: Nº '))
    valor_2 = float(input('Informe o segundo valor: Nº '))
    
    #Fórmula
    subtracao = (valor_1-valor_2)

    print(f'A subtração entre, {valor_1:.2f} - {valor_2:.2f}: = {subtracao:.2f}') 
    print('\n')
elif opcao == 3:
    print('INFORME OS VALORES PARA MULTIPLICAÇÃO')
    print('\n')
    valor_1 = float(input('Informe o primeiro valor: Nº '))
    valor_2 = float(input('Informe o segundo valor: Nº '))
    
    #Fórmula
    multiplicacao = (valor_1*valor_2)

    print(f'A multiplicação entre, {valor_1:.2f} * {valor_2:.2f}: = {multiplicacao:.2f}') 
    print('\n')
elif opcao == 4:
    print('INFORME OS VALORES PARA DIVISÃO')
    print('\n')
    valor_1 = float(input('Informe o primeiro valor: Nº '))
    valor_2 = float(input('Informe o segundo valor: Nº '))
    
    #Fórmula
    divisao = valor_1/valor_2

    print(f'A divisão entre, {valor_1:.2f} / {valor_2:.2f}: = {divisao:.2f}') 
    print('\n')


