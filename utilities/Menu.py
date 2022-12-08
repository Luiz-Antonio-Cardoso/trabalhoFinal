
#Recebe como argumentos: Opções do menu, Nome do Menu e o texto presente no input ao fim do menu.
def menu(op = [], nome = "menu", selecao = 'Digite uma das opções: '):
    pontos = "-----"

    print(pontos, nome, pontos)

    #Utiliza um if para verificar se existe alguma opção
    #e usa um laço de repetição para percorrer o array de opções
    #colocando o numero de cada opção e formatando no formato
    # Index - Opção.
    if len(op) != 0:        
        for i in op:
            intro = [(op.index(i)+1), "-"]
            print(intro[0],intro[1], i)
    
    #Utiliza o input no final do menu, caso não passe nenhum 
    #input como argumento ele coloca por padrão uma mensagem genérica
    opcao = input(selecao)
    return opcao