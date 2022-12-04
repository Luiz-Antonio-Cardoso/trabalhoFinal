from utilities.checaTamanho import retorna_id
from utilities.checaTamanho import checa_tamanho
from utilities.Menu import menu
from utilities.formatQuery import formatQuery
from database.selectByCpf import select_cpf
from database.createTables import *
from database.updateFunction import *

import pandas as pd
from IPython.display import display

import sys
sys.path.append('./')


def realiza_manutencao():

    selectByCpf = select_cpf('REALIZAR MANUTENÇÃO')
    listaManutencoesCpf = selectByCpf[0]
    cpfPesquisa = selectByCpf[1]
    query = selectByCpf[2]
    nome = selectByCpf[3]

    if int(checa_tamanho(listaManutencoesCpf) > 1):
        df = pd.read_sql_query(query, conn)
        df.columns = ['Id','Nome', 'CPF', 'Tipo de Veiculo', 'Detalhe', 'Valor', 'Descrição', 'Data de Entrada', 'Status']
        print(df)

        id = int(menu([], nome, 'Digite o ID da manutenção que você deseja realizar: '))
        update_function('M', 'id', id)
    elif int(checa_tamanho(listaManutencoesCpf) == 1):
        update_function('M', 'cpf', cpfPesquisa)
    else:
        print('Não há manutenções para esse CPF')
