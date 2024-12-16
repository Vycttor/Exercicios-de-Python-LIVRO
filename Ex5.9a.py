'''
Claro! Vamos entender a questão passo a passo, sem resolver:

O que o exercício pede?
Você deve criar um programa que:

Leia dois números: o primeiro número será o dividendo e o segundo será o divisor.

Calcule dois resultados:

Divisão inteira (ou quociente): Quantas vezes o divisor cabe no dividendo.
Resto da divisão: O que "sobra" depois de subtrair o divisor várias vezes do dividendo.
Restrições importantes:

Não usar operadores de multiplicação (*), divisão (/) ou módulo (%).
Use apenas soma (+) e subtração (-) para calcular o resultado.
Como entender a divisão inteira e o resto?
Divisão inteira (quociente): É o número de vezes que o divisor pode ser subtraído do dividendo até que o valor restante seja menor que o divisor.
Exemplo: 
20
÷
4
=
5
20÷4=5, porque você pode subtrair 4 cinco vezes de 20.
Resto: É o valor que sobra depois que você subtrai o divisor tantas vezes quanto possível.
Exemplo: 
22
÷
4
22÷4:
4
4 cabe 5 vezes em 
22
22, sobrando 2. O resto é 2.
Passos para resolver o exercício:
Inicialize variáveis:

Uma variável para contar o número de subtrações (o quociente).
Outra variável para armazenar o valor restante (o resto).
Repita a subtração:

Enquanto o dividendo for maior ou igual ao divisor, subtraia o divisor do dividendo.
A cada subtração, aumente o contador do quociente.
Pare quando não puder mais subtrair:

O valor restante do dividendo será o resto.
O contador mostrará o quociente.
Exemplo para ilustrar:
Se os números forem 20 (dividendo) e 4 (divisor):

Comece com o dividendo = 20.
Subtraia 4 sucessivamente:
20
−
4
=
16
20−4=16 (quociente = 1)
16
−
4
=
12
16−4=12 (quociente = 2)
12
−
4
=
8
12−4=8 (quociente = 3)
8
−
4
=
4
8−4=4 (quociente = 4)
4
−
4
=
0
4−4=0 (quociente = 5)
Aqui, o quociente é 5 e o resto é 0.

Resumo:
Objetivo: Imprimir o quociente e o resto.
Restrições: Usar apenas soma e subtração.
Lógica principal: Subtraia o divisor repetidamente do dividendo, conte as subtrações e guarde o valor final como resto.
'''