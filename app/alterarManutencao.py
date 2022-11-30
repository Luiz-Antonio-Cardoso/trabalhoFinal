import sys
sys.path.append('./')

import database.createTables
from utilities.formatQuery import formatQuery
from utilities.Menu import menu
import sqlite3


def altera_manutencao():
    conn = sqlite3.connect("db-oficina")

    nome = 'ALTERAR MANUTENÇÃO'
    
    cpfPesquisa = int(menu([], nome, 'Digite o CPF (apenas números) associados a manutenção que você deseja pesquisar: '))

    # query seleção pelo CPF
    query = conn.execute(
        'SELECT COUNT() FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))


        
    query = conn.execute(
            'SELECT id, nome, detalhe, tipoVeiculo, valor, descricao FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))        
  
    id = int(menu(query.fetchall(), nome, "Selecione o id da manutenção que deseja alterar(Primeiro valor): "))

    query = conn.execute(
            'SELECT detalhe, tipoVeiculo, valor, descricao, nome FROM manutencao WHERE id = {0}'.format(id))
    
    for i in query.fetchall():
        print(i)

    escolha_id = ['Detalhe', 'Tipo de veiculo','Descrição', 'Valor', 'Nome']
    escolha = int(menu(escolha_id, nome, 'Escolha o que deseja alterar:'))

    valores = {}

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
