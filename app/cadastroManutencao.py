import sys
sys.path.append('./')
from database.createTables import *

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