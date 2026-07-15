'''
Ex. 5.15 Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:

Código Preço
  1    0,50
  2    1,00 
  3    4,00
  5    7,00
  9    8,00

Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a messagem de erro "Código invalido"

'''

value = 0;
# array to verify if the number typed exist
Product_Codes = [0,1,2,3,5,9] 

while True: 
  
  print('''\n
 Código Preço
  1    0,50
  2    1,00 
  3    4,00
  5    7,00
  9    8,00

''')
  # Try: check if the user provided a valid number.
  try:
   # Use must provide a valid number
   code = int(input("Type the product code or 0 to exit: "))

   if code not in Product_Codes:
     print('Please type a valid number')
     print('0 to exit or select a number to continue')
     continue
   
  except ValueError:
    print('Please type a valid number')
    print('0 to exit or select a number to continue')
    continue
  

  if code == 0:
    break
  else:
    if code == 1:
      quantity = int(input('Select the product quantity: '))
      price = quantity * 0.5
      value += price
      print(f'\n Purchase value in the moment')
      print(f'Value R$ {value:.2f}')
    elif code == 2:
      quantity = int(input('Select the product quantity: '))
      price = quantity * 1
      value += price
      print(f'\n Purchase value in the moment')
      print(f'Value R$ {value:.2f}')
    elif code == 3:
      quantity = int(input('Select the product quantity: '))
      price = quantity * 4
      value += price
      print(f'\n Purchase value in the moment')
      print(f'Value R$ {value:.2f}')
    elif code == 5:
      quantity = int(input('Select the product quantity: '))
      price = quantity * 7
      value += price
      print(f'\n Purchase value in the moment')
      print(f'Value R$ {value:.2f}')
    elif code == 9:
      quantity = int(input('Select the product quantity: '))
      price = quantity * 8
      value += price
      print(f'\n Purchase value in the moment')
      print(f'Value R$ {value:.2f}')
      
      

print('##########################')
print(f'\n Total to pay R$ {value:.2f}')  
print('\n##########################')
        
