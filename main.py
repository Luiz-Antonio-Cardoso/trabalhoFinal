# imports
from exit import sair
from database.createTables import *
# end imports


criarTabela()

# region=== Variáveis/Banco - ESCOPO GLOBAL ===
# declara tudo o que for global AQUI


# endregion

# region === função formatar query ===



# endregion

# region === função de sair do programa ===




# endregion

# region === função de cadastrar manutenção ===


def cadastro_manutencao():
    manutencao = {}

    cadastro = False

    id = conn.execute("SELECT COUNT() FROM manutencao")
    id = id.fetchone()[0]

    print('\n-----CADASTRO DE MANUTENÇÃO-----\n')

    manutencao['id'] = (id)

    print(manutencao['id'])

    manutencao['nome'] = input("Digite o nome do cliente: ")
    manutencao['cpf'] = input("Digite o cpf do cliente (Apenas numeros): ")
    manutencao['tipoVeiculo'] = input(
        "Digite o tipo de veiculo (C – Carro, M – Moto, O – Outro): ")
    manutencao['detalhe'] = input("Digite os detalhes do veiculo: ")
    manutencao['valor'] = float(input("Digite o valor do orçamento: "))
    manutencao['descricao'] = input("Digite os detalhes do serviço: ")
    manutencao['dataEntrada'] = input(
        "Digite a data de entrada do veiculo (dia/mes/ano): ")
    manutencao['dataSaida'] = input(
        "Digite a data de saida do veiculo (dia/mes/ano): ")
    manutencao['status'] = "A"

    if manutencao['nome'] != '' and manutencao['cpf'] != '' and manutencao['detalhe'] != '' and manutencao['valor'] != '' and manutencao['dataEntrada'] != '':
        query = "INSERT INTO manutencao VALUES {0}  ".format(
            manutencao.values())
        query = query.replace("dict_values", "")
        query = query.replace("[", "")
        query = query.replace("]", "")
        print(conn.execute(query))
        print('Cadastro realizado com sucesso!')

        conn.commit()

        cadastro = True
    else:
        cadastro = print(
            "Os campos:\n Nome,\n cpf,\n detalhe,\n valor,\n data de entrada\n são obrigatorios, tente novamente.")

    selectManutencao = conn.execute("SELECT * FROM manutencao")
    print(selectManutencao.fetchall())

    return cadastro
# endregion

# region ===REALIZAR MANUTENÇÃO===
# •	Realizar manutenção.
# o	Nessa tela o usuário terá a opção de dar entrada no processo de manutenção.
# o	Para isso o usuário deverá realizar a busca de manutenção pelo CPF.
# 	Caso exista mais de uma manutenção no CPF da pessoa, o usuário deverá escolher qual manutenção ele quer dar entrada (utilizar o id da manutenção).
# o	O processo de entrada na manutenção é um processo automático, sendo necessário apenas alterar o STATUS da manutenção de A – Aguardando para manutenção para M – Em manutenção.
# o	O sistema deverá apresentar a mensagem de realização, ex: ‘A manutenção (id:8521) está sendo iniciada !!!’.


def realiza_manutencao():

    countManutencao = 0

    print('\n-----REALIZAR MANUTENÇÃO-----')
    cpfPesquisa = int(input(
        '\nDigite o CPF (apenas números) associados a manutenção que você deseja pesquisar: \n'))

    query = conn.execute(
        'SELECT COUNT() FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))

    countManutencao = formatQuery(query)

    print('TESTE FUNCAO FORMAT {0}'.format(countManutencao))
    print('cpf pesquisa {0}'.format(cpfPesquisa))

    if countManutencao == 1:
        query = conn.execute('''UPDATE manutencao
                                set status = 'M'
                                WHERE cpf = {0}'''.format(cpfPesquisa))
        print('Manutenção atualiza para status = "M"')
    elif countManutencao > 1:
        # select
        query = []
        id = []
        query = conn.execute(
            'SELECT id, detalhe, tipoVeiculo, valor, descricao, status FROM manutencao WHERE cpf = {0}'.format(cpfPesquisa))
        for row in query:
            print(row)
        query = conn.execute(
            'SELECT detalhe, tipoVeiculo, valor, descricao, nome FROM manutencao')
        for row in query.fetchall():
            valores = {}
            querys = []
            valores['detalhe'] = row[0]
            valores['tipoVeiculo'] = row[1]
            valores['valor'] = row[2]
            valores['descricao'] = row[3]
            valores['nome'] = row[4]
            querys.append(valores)

        escolha = int(input('\nEscolha uma das manutenções para dar entrada (ID - primeiro valor): '))

        query = conn.execute('''UPDATE manutencao
                                set status = 'M'
                                WHERE id = {0}'''.format(escolha))
        conn.commit()
        print('Manutenção atualiza para status = "M"')

    else:
        print('\nNão existem manutenção registradas nesse CPF!')

    return countManutencao

# region ===MENU PRINCIPAL===
def menu_principal():

    op = True
    while op == True:
        print('\n-----MENU PRINCIPAL-----')
        print('\nSelecione as seguintes opções para prosseguir:')
        print('1 - Cadastrar manutenção \n2 - Alterar manutenção')
        print('3 - Realizar manutenção \n4 - Finalizar manutenção')
        print('5 - Relatórios \n6 - Sair')

        opcao = int(input('Digite uma das opções: '))
        if (opcao == 1):
            cadastro_manutencao()
        elif (opcao == 2):
            altera_manutencao()
        elif (opcao == 3):
            realiza_manutencao()
        # elif(opcao == 4):
        #   finaliza_manutencao()
        # elif(opcao == 5):
        #   relatorios()
        elif (opcao == 6):
            sair()
        else:
            print('\n\nOpção inválida, por favor digite uma opção verdadeira.\n\n')


menu_principal()

# endregion
