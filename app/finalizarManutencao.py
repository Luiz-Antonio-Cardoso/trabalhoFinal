import sys
sys.path.append('./')

from database.createTables import *
from utilities.formatQuery import formatQuery
from utilities.Menu import menu
from utilities.checaTamanho import checa_tamanho
from utilities.checaTamanho import retorna_id
from datetime import date

def finaliza_manutencao():
    nome = 'FINALIZAR MANUTENÇÃO'
    cpfPesquisa = int(menu('',nome,'Digite o CPF (apenas números) associados a manutenção que você deseja pesquisar: '))

    query = conn.execute(
            'SELECT id, nome, detalhe, tipoVeiculo, valor, descricao, status FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))        

    listaManutencoesCpf = query.fetchall()

    if checa_tamanho(listaManutencoesCpf):
        pos = int(menu(listaManutencoesCpf, nome))
        id = retorna_id(listaManutencoesCpf, pos)
    else:
        id = retorna_id(listaManutencoesCpf, 1)

    query = conn.execute('''UPDATE manutencao SET status == {0} WHERE id = {1}'''.format(
                'F', id))
    conn.commit()
    print('Status alterado com sucesso!')
    query = conn.execute('''SELECT dataEntrada, dataSaida FROM manutencao WHERE id = {0}'''.format(id))

    for a in query.fetchall():
        dataInicio = a[0]
        dataFinal = a[1]


    # falta splitar as datas em array e passar como paramentro, date(ano, mes, dia)

    dataInicio = date(2014, 7, 2)
    dataFinal = date(2014, 7, 11)