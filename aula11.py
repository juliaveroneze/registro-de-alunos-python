import os

palavra = 'abacaxi'
tentativa_qtd = 0
tentativa_acert = ''

while True:
   
    tentativa = input('Digite uma letra: ').lower()

    if len(tentativa) != 1 or not tentativa.isalpha():
        print('⚠️  Digite apenas UMA letra!')
        continue

    if tentativa in tentativa_acert:
        print(f'⚠️  Você já tentou a letra "{tentativa}".')
        continue

    tentativa_qtd += 1

    if tentativa in palavra:
        print('✅ Letra correta!')
        tentativa_acert += tentativa
    else:
        print(f'❌ Você errou! Esta é a tentativa número {tentativa_qtd}')

    palavra_formada = ''
    for letra in palavra:
        if letra in tentativa_acert:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(f'Palavra: {palavra_formada}')

    if palavra_formada == palavra:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'🎉 Você acertou a palavra "{palavra}" em {tentativa_qtd} tentativas!')
        break
