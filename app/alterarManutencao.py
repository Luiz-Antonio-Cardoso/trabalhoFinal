from database.createTables import conn
from utilities.formatQuery import formatQuery

def altera_manutencao():
    print('\n-----ALTERAR MANUTENÇÃO-----')
    cpfPesquisa = int(input(
        '\nDigite o CPF (apenas números) associados a manutenção que você deseja pesquisar: \n'))

    query = conn.execute(
        'SELECT COUNT() FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))

    if (formatQuery(query) > 1):
        query = conn.execute(
            'SELECT id, detalhe, tipoVeiculo, valor, descricao FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))
        for row in query.fetchall():
            print(row)
        id = int(
            input('\nEscolha uma das manutenções para dar entrada (ID - primeiro valor): '))
        query = conn.execute(
            'SELECT detalhe, tipoVeiculo, valor, descricao, nome FROM manutencao WHERE id = {0}'.format(id))
        for row in query.fetchall():
            valores = {}
            querys = []
            valores['detalhe'] = row[0]
            valores['tipoVeiculo'] = row[1]
            valores['valor'] = row[2]
            valores['descricao'] = row[3]
            valores['nome'] = row[4]
            querys.append(valores)
        escolha = int(input(
            "\nEscolha o que deseja alterar:\n1 - Detalhe\n2 - Tipo de Veiculo\n3 - Valor\n4 - Descrição\n5 - Nome\n"))
        if (escolha == 1):
            valores['detalhe'] = input("Digite o novo detalhe do veiculo: ")
            query = conn.execute('''UPDATE manutencao SET detalhe = '{0}' WHERE id = {1}'''.format(
                valores['detalhe'], id))
            conn.commit()
            print('Detalhe alterado com sucesso!')
        elif (escolha == 2):
            valores['tipoVeiculo'] = input("Digite o novo tipo de veiculo: ")
            query = conn.execute('''UPDATE manutencao SET tipoVeiculo = '{0}' WHERE id = {1}'''.format(
                valores['tipoVeiculo'], id))
            conn.commit()
            print("Tipo de veiculo alterado com sucesso!")
        elif (escolha == 3):
            valores['valor'] = input("Digite o novo valor: ")
            query = conn.execute('''UPDATE manutencao SET valor = '{0}' WHERE id = {1}'''.format(
                valores['valor'], id))
            conn.commit()
            print("Valor alterado com sucesso!")
        elif (escolha == 4):
            valores['descricao'] = input("Digite a nova descrição: ")
            query = conn.execute('''UPDATE manutencao SET descricao = '{0}' WHERE id = {1}'''.format(
                valores['descricao'], id))
            conn.commit()
            print("Descrição alterada com sucesso!")
        elif (escolha == 5):
            valores['nome'] = input("Digite o novo nome: ")
            query = conn.execute('''UPDATE manutencao SET nome = '{0}' WHERE id = {1}'''.format(
                valores['nome'], id))
            conn.commit()
            print("Nome alterada com sucesso!")
