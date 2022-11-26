from database.createTables import *
from utilities.facade import *

def finaliza_manutencao():

    
    countManutencao = 0

    print('\n-----FINALIZAR MANUTENÇÃO-----')
    cpfPesquisa = int(input(
        '\nDigite o CPF (apenas números) associados a manutenção que você deseja pesquisar: \n'))

    query = conn.execute(
        'SELECT COUNT() FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))

    countManutencao = formatQuery(query)

    print('TESTE FUNCAO FORMAT {0}'.format(countManutencao))
    print('cpf pesquisa {0}'.format(cpfPesquisa))

    if countManutencao == 1:
        query = conn
        