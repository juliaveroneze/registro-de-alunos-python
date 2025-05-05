listas = [
    [1, 2, 3],
    [10, 20, 30],
    [5, 90, 25],
    [100, 27, 300],
    [7, 14]
]
def rep():
    repetidos = set()
    primeiro_repetido = None
    for sublista in listas:
        for numero in sublista:
            if numero in repetidos:
                primeiro_repetido = numero
            repetidos.add(numero)
        if primeiro_repetido is not None:
            print(f'numero repetido: {primeiro_repetido}')
            break
        else:
            print('-1')
            break

    

rep()