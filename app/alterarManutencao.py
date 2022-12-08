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

    nome = 'ALTERAR MANUTENÇÃO'
    selectByCpf = select_cpf(nome)

    listaManutencoesCpf = selectByCpf[0]
    cpfPesquisa = selectByCpf[1]
    query = selectByCpf[2]
    nome = selectByCpf[3]

    #Checa se a pesquisa no banco retorna mais de uma linha
    if int(checa_tamanho(listaManutencoesCpf) > 1):
        #Utiliza o pandas para mostras a tabela na tela
        df = pd.read_sql_query(query, conn)
        df.columns = ['Id','Nome', 'CPF', 'Tipo de Veiculo', 'Detalhe', 'Valor', 'Descrição', 'Data de Entrada', 'Status']
        print(df)
        id = menu([],nome, 'Digite o ID da manutenção desejada.' )

    #Verifica se a pesquisa tem apenas uma linha e retorna o id dessa unica linha
    elif int(checa_tamanho(listaManutencoesCpf) == 1):
        id = retorna_id(query, 1)
    #Caso a pesquisa nao retorne nenhum resultado informa que nao 
    #existem manutenções nesse cpf
    else:
        print('Não há manutenções para esse CPF')
        #Da opção de voltar para o menu principal ou tentar novamente
        erro = menu(['Menu Principal', 'Tentar novamente'], nome)
        if erro == 1:
            menu_principal()
        elif erro == 2:
            altera_manutencao()


    #Usuario escolhe qual campo da tabela deseja alterar
    escolha_id = ['Detalhe', 'Tipo de veiculo','Descrição', 'Valor', 'Nome']
    escolha = int(menu(escolha_id, nome, 'Escolha o que deseja alterar: '))

    valores = {}

    #Utiliza a opção desejada para fazer a alteração 
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
