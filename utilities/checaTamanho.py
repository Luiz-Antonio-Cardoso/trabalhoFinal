#Recebe e query e a posição escolhida da linha
# após isso percorre o array e devolve a opção de ID da linha 
def retorna_id( query, posicao ):
    id = query[posicao][0]

    return id


#Recebe como parametro o cursor da query do banco de dados
# e retorna a quantidade de linhas presentes no array
def checa_tamanho( query ):
    tamanho = 0
    for a in query:
        tamanho += 1

    return tamanho
    # if i == 1:
    #     return False
    # else:
    #     return True