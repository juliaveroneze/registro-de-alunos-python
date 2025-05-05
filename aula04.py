nome = input('digite seu nome: ')
idade = input('digite sua idade: ')


if nome == '' and idade == '':
    print('desculpe, campos vazio')
else:
    print('continuar o programa')

print(f'seu nome é: {nome}')

print(f'seu nome invertido é {nome[::-1]}')

if ' ' in nome:
    print(f'o nome: {nome} contém espaço')
else:
    print(f'o nome: {nome} não contém espaço')

nome_sem_espaco = nome.replace(' ',"") 
print(f'seu nome contém {len(nome_sem_espaco)} letras')

print(f'a primeira letra do seu nome é {nome[0]}')

print(f'a ultima letra do seu nome é {nome[-1]}')
