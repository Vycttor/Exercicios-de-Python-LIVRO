#Digite a seguinte expressão no interpretador
#10%3*10**2+1-10*4/2

print("Qual modulo de 10%3 ?")
#Abaixo o calculo do modulo
modulo= 10%3
print("O modulo é =:", modulo)

print ("Qual o resultado de 10**2? ")

#Abaixo calculo da exponenciação
expot = 10**2
print ("O resultado da exponenciação é =: ",expot)

print ("Qual a resutado de 1-10? ")

#Abaixo calculo da subtração
sub = 1 - 10
print ("O valor da subtração é =: ",sub)

print ("Qual o resultado de 4/2? ")
#calculo da divisão
div = 4/2

print ("O valor da divisão é =:", div)
#(10%3)*(10**2)+(1-10)*(4/2)
print ("(10%3)*(10**2)+(1-10)*(4/2)")
result = (modulo*expot*div)+sub
print ("O resultado é =: ",result)
