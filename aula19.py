def mult(*args):
    novo = 1
    for numeros in args:
        novo *= numeros 
    return novo
    
numerosd = mult(1,2,3,4,5)    
print(numerosd)

def par_impar(n ):
    parImpar = f'{n} é par' if n % 2 == 0 else f'{n} é impar'
    return parImpar

print(par_impar(6))