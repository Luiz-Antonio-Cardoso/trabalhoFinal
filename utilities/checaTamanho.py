def retorna_id( query, posicao ):
    for a in query:
        if (query.index(a)+1) == posicao: 
            b = a     
    return b[0]

def checa_tamanho( query ):
    i = 0
    for a in query:
        i += 1

    return i
    # if i == 1:
    #     return False
    # else:
    #     return True