import sys
sys.path.append('./')

import pandas as pd
from database.createTables import *
from IPython.display import display

def relatorios(where = ''):
    
    #usando o pandas para criar um dataframe formatado com as informacoes da tabela manutencao
    df = pd.read_sql_query("SELECT * FROM manutencao {0}".format(where), conn)
    
    #arrumar cabeçalho
    df.columns = ['Id','Nome', 'CPF', 'Tipo de Veiculo', 'Detalhe', 'Valor', 'Descrição', 'Data de Entrada', 'Data de Saida', 'Status']
    
    #espaçamento entre colunas
    # pd.set_option('display.width', 2000) 
    print(df)

relatorios('A')