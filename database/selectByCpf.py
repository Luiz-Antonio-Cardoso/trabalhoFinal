from database.createTables import *

import sys
sys.path.append('./')

from utilities.Menu import menu

#vai retornar uma lista com as manutenções do cpf pesquisado e o cpf pesquisado
# e a query que foi executada
def select_cpf(nome):

    cpfPesquisa = menu('',nome,'Digite o CPF (apenas números) associados a manutenção que você deseja pesquisar: ')

    query = ('SELECT * FROM manutencao WHERE cpf = "{0}"'.format(cpfPesquisa))
    queryFinalizada = (conn.execute(query).fetchall())

    listaManutencoesCpf = [queryFinalizada, cpfPesquisa, query, nome]

    return listaManutencoesCpf
