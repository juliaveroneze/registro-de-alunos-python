entrada = input('digite [E]ntrar ou [S]air: ')

senha_permitida = '123'
senha_digitada = input('senha: ')

if entrada == 'E' and senha_digitada == senha_permitida:
    print('sistema acessado')
elif entrada == 'S' and senha_digitada == senha_permitida:
    print('saiu do sitema')
elif senha_digitada != senha_permitida:
    print('senha inválida!')
else:
    print('precisa ser digitado uma das opções válidas')


#print(not 1)