numero = input('digite um numero para saber se é par ou ímpar: ')
impar = (int(numero) / 2) % 1

if impar:
    print('ímpar')
else:
    print('par')


horario = input('que horas são? ')
horario_int = int(horario)

manha = horario_int >= 0 and horario_int <= 11
tarde = horario_int >= 12 and horario_int <= 17
noite = horario_int >= 18 and horario_int <= 23

if manha:
    print('bom dia')
elif tarde:
    print('boa tarde')
elif noite:
    print('boa noite')
else:
    print('digite horários validos')


nome = input('digite seu primeiro nome: ')

nome_qtd_letras = len(nome)
nome_curto = nome_qtd_letras <= 4
nome_normal = nome_qtd_letras >= 5 and nome_qtd_letras <= 6
nome_grande = nome_qtd_letras > 6
if nome_curto:
    print(f'{nome} é um nome curto')
elif nome_normal:
    print(f'{nome} é um nome normal')
elif nome_grande:
    print(f'{nome} é um nome grande')
else:
    print('digite um valor válido')