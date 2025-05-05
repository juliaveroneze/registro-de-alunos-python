import os

lista = []
while True:
    opcao = input('1- Inserir\t2- Apagar\t3- Listar\nSelecione uma opção: ')
    if opcao == '1':
        add_item = input('Qual item deseja adicionar: ')
        lista.append([add_item])
        print('Seu item foi adicionado com sucesso!')

    elif opcao == '2':
        if not lista:
            print('Nada para apagar')
        else:
            apagar_item = input('Qual item deseja apagar: ')
            item_removido = False

            for item in lista:
                if item[0] == apagar_item:
                    lista.remove(item)
                    item_removido = True
                    print('Seu item foi removido com sucesso!')

            if not item_removido:
                print('Seu item não existe!')
            
    elif opcao == '3':
        if lista == []:
            print('Nada para listar')
        for indice, item in enumerate(lista):
            nome = item[0]
            print(f'{indice}) { nome.capitalize()}')
    else: 
        print('Por favor, digite 1, 2 ou 3!')
        

    saida = input('Deseja continuar?\n1- sim\t2-não\n')
    if saida == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    elif saida == '2':
        print('FIM!')
        break
    else:
        print('Digite uma opção válida!')
        break