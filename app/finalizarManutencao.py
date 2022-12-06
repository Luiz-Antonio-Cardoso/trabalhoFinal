import sys
sys.path.append('./')

from database.createTables import *
from utilities.Menu import menu
from database.updateFunction import *
from utilities.checaTamanho import checa_tamanho
from database.selectByCpf import select_cpf
from database.recuperaData import finaliza_data
import pandas as pd

def finaliza_manutencao():

    selectByCpf = select_cpf('FINALIZAR MANUTENÇÃO')
    listaManutencoesCpf = selectByCpf[0]
    cpfPesquisa = selectByCpf[1]
    query = selectByCpf[2]
    nome = selectByCpf[3]

    #fazer a verificação se a manutenção está com status diferente de 'M'

    if int(checa_tamanho(listaManutencoesCpf) > 1):
        df = pd.read_sql_query(query, conn)
        df.columns = ['Id','Nome', 'CPF', 'Tipo de Veiculo', 'Detalhe', 'Valor', 'Descrição', 'Data de Entrada', 'Data de Saida', 'Status']
        print(df)

        id = int(menu([], nome, 'Digite o ID da manutenção que você deseja realizar: '))
        update_function('F', 'id', id)
        finaliza_data(id)
        
    elif int(checa_tamanho(listaManutencoesCpf) == 1):
        update_function('F', 'cpf', cpfPesquisa)
        query = conn.execute('SELECT id FROM manutencao WHERE cpf = "{0}"'.format(cpfPesquisa))
        id = query.fetchone()[0]
        finaliza_data(id)

    else:
        print('Não há manutenções para esse CPF')