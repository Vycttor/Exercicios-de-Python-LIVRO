'''
Ex 5.6. Altere o progra anterior (pag 87), para exibir os resultados no mesmo formato de uma tabuada: 2 x 1 = 2, 2 x 2 = 4,...

'''
print('======='*2)
numero =  int(input('Tabuada: '))
print('======='*2)

cont = 1

while cont <= 10:
    print(f'{numero} x {cont} = {cont*numero}') 
    cont += 1
print('======='*2)    