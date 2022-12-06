import sys
sys.path.append('./')

from utilities.formatQuery import formatQuery
from utilities.Menu import menu
from utilities.checaTamanho import checa_tamanho
from utilities.checaTamanho import retorna_id

from database.selectByCpf import select_cpf
from database.updateFunction import *
import pandas as pd
from IPython.display import display

def altera_manutencao():

    selectByCpf = select_cpf('ALTERAR MANUTENÇÃO')

    listaManutencoesCpf = selectByCpf[0]
    cpfPesquisa = selectByCpf[1]
    query = selectByCpf[2]
    nome = selectByCpf[3]

    if int(checa_tamanho(listaManutencoesCpf) > 1):
        df = pd.read_sql_query(query, conn)
        df.columns = ['Id','Nome', 'CPF', 'Tipo de Veiculo', 'Detalhe', 'Valor', 'Descrição', 'Data de Entrada', 'Status']
        print(df)

        id = int(menu([], nome, 'Digite o ID da manutenção que você deseja alterar: '))
        update_function('M', 'id', id),
    elif int(checa_tamanho(listaManutencoesCpf) == 1):
        update_function('M', 'cpf', cpfPesquisa)
    else:
        print('Não há manutenções para esse CPF')

    # if checa_tamanho(listaManutencoesCpf):
    #     pos = int(menu(listaManutencoesCpf, nome))
    #     id = retorna_id(listaManutencoesCpf, pos)
    # else:
    #     id = retorna_id(listaManutencoesCpf, 1)

    # query = conn.execute(
    #         'SELECT detalhe, tipoVeiculo, valor, descricao, nome FROM manutencao WHERE id = {0}'.format(id))
    
    # for i in query.fetchall():
    #     print(i)

    escolha_id = ['Detalhe', 'Tipo de veiculo','Descrição', 'Valor', 'Nome']
    escolha = int(menu(escolha_id, nome, 'Escolha o que deseja alterar: '))

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
