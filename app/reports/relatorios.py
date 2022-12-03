import sys
sys.path.append('./')

import pandas as pd
from database.createTables import *
from IPython.display import display

def relatorios( option = '', where = ''):
    print(option, where)
    
    #usando o pandas para criar um dataframe formatado com as informacoes da tabela manutencao
    #parametro option vai escolher a query que sera executada
    #parametro where vai escolher o filtro que sera aplicado na query
    df = pd.read_sql_query("SELECT {0} FROM manutencao {1}".format(option, where), conn)
    
    #arrumar cabeçalho
    if (option == 'SUM(valor)'):
        df.columns = ['Total']
    else:
        df.columns = ['Id','Nome', 'CPF', 'Tipo de Veiculo', 'Detalhe', 'Valor', 'Descrição', 'Data de Entrada', 'Data de Saida', 'Status',]
    
    #espaçamento entre colunas
    # pd.set_option('display.width', 2000) 
    print(df)