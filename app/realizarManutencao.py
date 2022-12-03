from utilities.checaTamanho import retorna_id
from utilities.checaTamanho import checa_tamanho
from utilities.Menu import menu
from utilities.formatQuery import formatQuery
from database.createTables import *

import pandas as pd
from IPython.display import display

import sys
sys.path.append('./')


def realiza_manutencao():

    nome = 'REALIZAR MANUTENÇÃO'
    cpfPesquisa = menu(
        [], nome, 'Digite o CPF (apenas números) associados a manutenção que você deseja pesquisar: ')

    query = 'SELECT * FROM manutencao WHERE cpf = "{0}"'.format(cpfPesquisa)

    listaManutencoesCpf = conn.execute(query).fetchall()

    # if checa_tamanho(listaManutencoesCpf):
    #     pos = menu(listaManutencoesCpf, nome)
    #     id = retorna_id(listaManutencoesCpf, pos)
    # else:
    #     id = retorna_id(listaManutencoesCpf, 1)

    if int(checa_tamanho(listaManutencoesCpf) > 1):
        df = pd.read_sql_query(query, conn)
        df.columns = ['Id','Nome', 'CPF', 'Tipo de Veiculo', 'Detalhe', 'Valor', 'Descrição', 'Data de Entrada', 'Data de Saida', 'Status']
        print(df)

        id = int(menu([], nome, 'Digite o ID da manutenção que você deseja realizar: '))
        update_manutencao('id', id)
    elif int(checa_tamanho(listaManutencoesCpf) == 1):
        update_manutencao('cpf', cpfPesquisa)
    else:
        print('Não há manutenções para esse CPF')


def update_manutencao(option, arg):
    print(option, arg)
    conn.execute('''
                UPDATE manutencao
                set status = 'M'
                WHERE {0} = "{1}"
                '''.format(option, arg))
    conn.commit()
    return print('Manutenção atualiza para status = "M"')
