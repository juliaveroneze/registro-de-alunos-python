#A primeira linha contém a soma dos dois números.
#A segunda linha contém a diferença dos dois números (primeiro - segundo).
#A terceira linha contém o produto dos dois números.

n = int(input('n: '))

n = range(0, n, 1)
for numero in n:
    quadrado = pow(numero, 2)
    print(quadrado)
    