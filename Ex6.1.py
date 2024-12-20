'''
Ex. 6.1. Modifique o Programa 6.2 pag.99 para ler 7 notas em vez de 5.
'''


notas = [0,0,0,0,0,0,0] #Lista 7 elementos
soma = x = 0
while x < 7:
    notas[x] = float(input(f'Nota {x}: '))#ira colocar 7 elementos na lista.
    soma += notas[x]
    x = x + 1

print('\n')
x = 0
while x < 7:
    print(f'Nota {x}: {notas[x]:6.2f}')
    x = x + 1
print(f'Média: {soma /x:5.2f}')
