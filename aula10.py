frase = input('digite uma frase: ')
qtd_apareceu_mais = 0
letra_apareceu_mais = ''
frase_sem_espaco = frase.replace(' ','')
i = 0
while i < len(frase_sem_espaco):
    letra = frase_sem_espaco[i]
    qtd = frase_sem_espaco.count(letra)
    
    if qtd_apareceu_mais < qtd:
        qtd_apareceu_mais = qtd
        letra_apareceu_mais = letra

    i += 1
print(f'letra que mais apareceu foi "{letra_apareceu_mais}" que apareceu {qtd_apareceu_mais} vezes')