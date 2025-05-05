cpf = '111.111.111-11'

cpf_limpo = cpf.replace('.', '').replace('-', '')

if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
    print('CPF INVÁLIDO')
else:
    cpf_numeros = [int(digito) for digito in cpf_limpo]

#Cálculo para primeiro dígito
i_digito_1 = 10 
multiplicados_1 = []

for num in cpf_numeros:
    multiplicados_1.append(num * i_digito_1)
    i_digito_1 -= 1
    if i_digito_1 == 1: break

soma_multiplicados_1 = (sum(multiplicados_1))* 10
resto_1 = soma_multiplicados_1 % 11
digito_1 = 0 if resto_1 > 9 else resto_1
print('O primeiro dígito do CPF é:', digito_1)

cpf_com_digito_1 = cpf_numeros[:9] + [digito_1]

#Cálculo para segundo dígito
i_digito_2 = 11
multiplicados_2 = []

for num in cpf_com_digito_1:
    multiplicados_2.append(num * i_digito_2)
    i_digito_2 -= 1
    
soma_multiplicados_2 = (sum(multiplicados_2)) * 10
resto_2 = soma_multiplicados_2 % 11
digito_2 = 0 if resto_2 > 9 else resto_2
print('O segundo dígito do CPF é:', digito_2)


if digito_1 == cpf_numeros[9] and digito_2 == cpf_numeros[10]:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')