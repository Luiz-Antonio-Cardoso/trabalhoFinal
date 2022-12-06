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
        #vai mostrar uma tabela com as manutenções e vai pedir para o usuário digitar o id da
        #manutenção que ele deseja realizar
        df = pd.read_sql_query(query, conn)
        df.columns = ['Id','Nome', 'CPF', 'Tipo de Veiculo', 'Detalhe', 'Valor', 'Descrição', 'Data de Entrada', 'Data de Saida', 'Status']
        print(df)

        id = int(menu([], nome, 'Digite o ID da manutenção que você deseja realizar: '))
        update_function('F', 'id', id)
        #funcao que vai atualizar a data de saida da manutenção
        finaliza_data(id)
        
    elif int(checa_tamanho(listaManutencoesCpf) == 1):
        #se a lista de manutenções do cpf pesquisado for igual a 1, vai atualizar
        #o status da manutenção para 'F'
        update_function('F', 'cpf', cpfPesquisa)
        query = conn.execute('SELECT id FROM manutencao WHERE cpf = "{0}"'.format(cpfPesquisa))
        id = query.fetchone()[0]
        #funcao que vai atualizar a data de saida da manutenção
        finaliza_data(id)

    else:
        print('Não há manutenções para esse CPF')