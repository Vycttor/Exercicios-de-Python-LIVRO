'''
Ex. 5.14. Escreva um programa que leia números inteiros do teclado. O programa deve ler os números  até que o usuário digite 0 (zero). No fina da execução,  exiba a quantidade de números digitados, assim como a soma e a média aritmética.
'''

soma = cont = 0

while True:
    numero = int(input('Digite o número a somar ou 0 para sair:[Nº/0] '))
    if numero == 0:
        break
    cont = cont + 1
    soma = soma + numero
print('\n')
print(f'Foram digitados {cont} números.')
print(f'A soma dos núemeros =  {soma}')
print(f'A média é = {soma/cont}')