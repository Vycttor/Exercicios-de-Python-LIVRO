#Função Adição do valor
def soma(a, b):
    c = a + b
    print("O resultado da soma é ", c)

#Função subtração do valor
def subt(a, b):
    c = a - b
    print("O resultado da subtração é ", c)

# Pede para o usuario digitar os valores para serem calculados.
print("Didigite dois valores para o calculo de Adição e Sbtração")
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

#Chama as funções.
soma(a, b)
subt(a, b)