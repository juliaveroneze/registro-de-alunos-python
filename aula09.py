while True:
    n1 = input('n1: ')
    n2 = input('n2: ')
    op = input('op: ')
    n_v = None
    try:
        n1f = float(n1)
        n2f = float(n2)
        n_v = True
    except:
        n_v = None

    if n_v is None:
        print('n invalido')
        continue
    
    
    if op not in '+-/*':
        print('op invalido')
        continue
        
    if len(op) != 1:
        print('permitido apenas 1 operador')

    if op == '+':
        print(f'a soma dos números é {n1f + n2f}')
    elif op == '-':
        print(f'a subtração dos números é {n1f - n2f}')
    elif op == '/':
        print(f'a divisão dos números é {n1f / n2f}')
        if n2 > n1:
            print('escolha um numero menor que o primeiro')
    elif op == '*':
        print(f'a multiplicação dos números é {n1f * n2f}')
        
    
    if input('sair: [s/n]').strip().lower().startswith('s') is True:
        break
    