# Programa converte semana em meses e meses em dias.

print('==='*15)
semanas = int(input('Informe as semanas: '))
print('==='*15)
print('\n')


#formulas
meses = semanas / 4.34
dias = meses * 30
print('==='*15)
print(f'{semanas} semanas equivale a {meses:.2f} meses')
print(f'{meses:.2f} meses equivale a {dias:.2f} dias')
print('==='*15)