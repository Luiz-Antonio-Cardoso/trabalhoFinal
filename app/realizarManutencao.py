import sys
sys.path.append('./')
from database.createTables import *
from utilities.formatQuery import formatQuery
from utilities.Menu import menu
from utilities.checaTamanho import checa_tamanho
from utilities.checaTamanho import retorna_id
def realiza_manutencao():


    nome = 'REALIZAR MANUTENÇÃO'
    cpfPesquisa = menu([], nome, 'Digite o CPF (apenas números) associados a manutenção que você deseja pesquisar: ')
   
    query = conn.execute(
            'SELECT id, nome, detalhe, tipoVeiculo, valor, descricao, status FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))   

    listaManutencoesCpf = query.fetchall()

    if checa_tamanho(listaManutencoesCpf):
        pos = int(menu(listaManutencoesCpf, nome))
        id = retorna_id(listaManutencoesCpf, pos)
    else:
        id = retorna_id(listaManutencoesCpf, 1)

    query = conn.execute('''UPDATE manutencao
                                set status = 'M'
                                WHERE id = {0}'''.format(id))
    print('Manutenção atualiza para status = "M"')    
