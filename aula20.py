def duplicar(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

n_duplicado = duplicar(3)
print(n_duplicado(2))
