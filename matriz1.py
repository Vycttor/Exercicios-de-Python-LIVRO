#Cria uma matriz quadradica vazia com duas posições.
matriz=[[0]*2]+[[1]*2]
# Imprime a matriz vazia
print(matriz)
# Solicita para o usuario o valor das martizes
matriz[0][0] = int(input("Didite o valor da posição 0.0 da matriz: "))
matriz[0][1] = int(input("Didite o valor da posição 0.1 da matriz: "))
matriz[1][0] = int(input("Didite o valor da posição 1.0 da matriz: "))
matriz[1][1] = int(input("Didite o valor da posição 1.1 da matriz: "))
# Imprime na tela os valores das matrizes
print (matriz)

