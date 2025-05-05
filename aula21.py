perguntas = [
    {
        'Questão': 'Quanto é 1+1: ',
        'Alternativas': [5, 6, 2, 4],
        'Correta': '2',
    },
    {
        'Questão': 'Quanto é 10/2: ',
        'Alternativas': [5, 6, 2, 4],
        'Correta': '5',
    },
]


def quest():
    for pergunta in perguntas:
        print(pergunta['Questão'])

        for i, alt in enumerate(pergunta['Alternativas']):
            print(f'{i+1}) {alt}')

        try:
            escolha = int(input('Digite a alternativa correta: '))
            resposta = pergunta['Alternativas'][escolha-1]
        except(ValueError, IndexError):
            print('entrada invalida!!!')
            continue

        if resposta == int(pergunta['Correta']):
            print('ACERTOU')
        else:
            print('ERROU')
        

quest()