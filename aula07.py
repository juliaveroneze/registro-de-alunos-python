#contador = 0

#while contador < 10:
#    contador += 1
#    print(contador)
operacao = input('[S]oma\n[Sub]tração\n[D]ivisão\n[M]ultiplicação\nescolha uma das operações: ')
n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))

if operacao == 'S':
    print(f'a soma dos números é {n1 + n2}')
elif operacao == 'Sub':
    print(f'a subtração dos números é {n1 - n2}')
elif operacao == 'D':
    print(f'a divisão dos números é {n1 / n2}')
    if n2 > n1:
        print('escolha um numero menor que o primeiro')
elif operacao == 'M':
    print(f'a multiplicação dos números é {n1 * n2}')

#tabuada com while

tabuada = int(input('qual n de taboada deseja? '))
contador = 0
while contador < 10:
    contador += 1
    print(f'{tabuada} X {contador} = {tabuada*contador}')