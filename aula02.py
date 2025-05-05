valor1 = input('digite o valor 1: ')
valor2 = input('digite o valor 2: ')

if valor1 > valor2:
    print(f'{valor1} é maior do que {valor2}')
elif valor1 < valor2:
    print(f'{valor2} é maior do que {valor1}')
elif valor1 == valor2:
    print(f'{valor1} e {valor2} são iguais')
else:
    print('digite valor válido')