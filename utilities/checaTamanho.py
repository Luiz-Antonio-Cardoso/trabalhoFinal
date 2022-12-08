#Recebe e query e a posição escolhida da linha
# após isso percorre o array e devolve a opção de ID da linha 
def retorna_id( query, posicao ):
    for a in query:
        if (query.index(a)+1) == posicao: 
            b = a     
    return b[0]


#Recebe como parametro o cursor da query do banco de dados
# e retorna a quantidade de linhas presentes no array
def checa_tamanho( query ):
    i = 0
    for a in query:
        i += 1

    return i
    # if i == 1:
    #     return False
    # else:
    #     return True