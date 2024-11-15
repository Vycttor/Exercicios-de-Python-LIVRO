#Ex 4.3 Escreva um programa que leia três números e que imprima o maior e o menor.

#Exercicio feito pelo Prof. Gustavo dia 25/10/2024

a = int(input('Informe um numero: '))
b = int(input('Informe outro numero: '))
c = int(input('Informe mais um numero: '))

#Verificando quem é o menor.
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c    

#Veificar quem é o maior.
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))