from database.createTables import *
from utilities.formatQuery import formatQuery

def realiza_manutencao():

    countManutencao = 0

    print('\n-----REALIZAR MANUTENÇÃO-----')
    cpfPesquisa = int(input(
        '\nDigite o CPF (apenas números) associados a manutenção que você deseja pesquisar: \n'))

    query = conn.execute(
        'SELECT COUNT() FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))

    countManutencao = formatQuery(query)

    print('TESTE FUNCAO FORMAT {0}'.format(countManutencao))
    print('cpf pesquisa {0}'.format(cpfPesquisa))

    if countManutencao == 1:
        query = conn.execute('''UPDATE manutencao
                                set status = 'M'
                                WHERE cpf = {0}'''.format(cpfPesquisa))
        print('Manutenção atualiza para status = "M"')
    elif countManutencao > 1:
        # select
        query = []
        id = []
        query = conn.execute(
            'SELECT id, detalhe, tipoVeiculo, valor, descricao, status FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))
        for row in query:
            print(row)
        query = conn.execute(
            'SELECT detalhe, tipoVeiculo, valor, descricao, nome FROM manutencao')
        for row in query.fetchall():
            valores = {}
            querys = []
            valores['detalhe'] = row[0]
            valores['tipoVeiculo'] = row[1]
            valores['valor'] = row[2]
            valores['descricao'] = row[3]
            valores['nome'] = row[4]
            querys.append(valores)

        escolha = int(input('\nEscolha uma das manutenções para dar entrada (ID - primeiro valor): '))

        query = conn.execute('''UPDATE manutencao
                                set status = 'M'
                                WHERE id = {0}'''.format(escolha))
        conn.commit()
        print('Manutenção atualiza para status = "M"')

    else:
        print('\nNão existem manutenção registradas nesse CPF!')

    return countManutencao
