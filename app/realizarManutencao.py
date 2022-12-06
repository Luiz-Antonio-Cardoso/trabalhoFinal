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

    #funcao que vai realizar a manutencao e vai retornar os informações para
    #melhor manipulação de dados
    
    selectByCpf = select_cpf('REALIZAR MANUTENÇÃO')

    listaManutencoesCpf = selectByCpf[0] #lista com as manutenções do cpf pesquisado
    cpfPesquisa = selectByCpf[1] #cpf pesquisado
    query = selectByCpf[2] #query que foi executada
    nome = selectByCpf[3] #nome da operação

    #se a lista de manutenções do cpf pesquisado for maior que 1, vai mostrar
    #uma tabela com as manutenções e vai pedir para o usuário digitar o id da
    #manutenção que ele deseja realizar
    if int(checa_tamanho(listaManutencoesCpf) > 1):
        df = pd.read_sql_query(query, conn)
        df.columns = ['Id','Nome', 'CPF', 'Tipo de Veiculo', 'Detalhe', 'Valor', 'Descrição', 'Data de Entrada', 'Status']
        print(df)

        id = int(menu([], nome, 'Digite o ID da manutenção que você deseja realizar: '))
        update_function('M', 'id', id)
    #se a lista de manutenções do cpf pesquisado for igual a 1, vai atualizar
    #o status da manutenção para 'M'
    elif int(checa_tamanho(listaManutencoesCpf) == 1):
        update_function('M', 'cpf', cpfPesquisa)
    else:
        print('Não há manutenções para esse CPF')
