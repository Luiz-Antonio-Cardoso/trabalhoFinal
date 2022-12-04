def menu(op = [], nome = "menu", selecao = 'Digite uma das opções: '):
    pontos = "-----"

    print(pontos, nome, pontos)

    if len(op) != 0:        
        for i in op:
            intro = [(op.index(i)+1), "-"]
            print(intro[0],intro[1], i)
    
    opcao = input(selecao)
    return opcao