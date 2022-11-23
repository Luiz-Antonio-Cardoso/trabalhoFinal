import sys
import sqlite3

#region=== Variáveis/Banco - ESCOPO GLOBAL ===
##declara tudo o que for global AQUI

aux = False

if aux == False:

  conn = sqlite3.connect("db-oficina")

  cursor = conn.cursor()

  cursor.execute('''CREATE TABLE manutencao (
                    id INTEGER PRIMARY KEY NOT NULL,
                    nome NVARCHAR(50) NOT NULL,
                    cpf NVARCHAR(11) NOT NULL,
                    tipoVeiculo NVARCHAR (50),
                    detalhe NVARCHAR(200) NOT NULL,
                    valor FLOAT NOT NULL,
                    descricao NVARCHAR (200) NOT NULL,
                    dataEntrada DATETIME NOT NULL,
                    dataSaida DATETIME NOT NULL,
                    status NVARCHAR(1) NOT NULL
                  );''')
  aux = True

#endregion

#region === função de sair do programa ===

def sair():
    return sys.exit('\nSaindo\n')

#endregion

#region === função de cadastrar manutenção ===
def cadastro_manutencao():
    manutencao = {} 

    cadastro = False

    id = conn.execute("SELECT COUNT() FROM manutencao")
    id = id.fetchone()[0]

    print('\n-----CADASTRO DE MANUTENÇÃO-----\n')

    manutencao['id'] = (id)

    print(manutencao['id'])

    manutencao['nome'] = input("Digite o nome do cliente: ")
    manutencao['cpf'] = int(input("Digite o cpf do cliente (Apenas numeros): "))
    manutencao['tipoVeiculo'] = input("Digite o tipo de veiculo (C – Carro, M – Moto, O – Outro): ")
    manutencao['detalhe'] = input("Digite os detalhes do veiculo: ")
    manutencao['valor'] = float(input("Digite o valor do orçamento: "))
    manutencao['descricao'] = input("Digite os detalhes do serviço: ")
    manutencao['dataEntrada'] = input("Digite a data de entrada do veiculo (dia/mes/ano): ")
    manutencao['dataSaida'] = input("Digite a data de saida do veiculo (dia/mes/ano): ")
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
        cadastro = print("Os campos:\n Nome,\n cpf,\n detalhe,\n valor,\n data de entrada\n são obrigatorios, tente novamente.")

    selectManutencao = conn.execute("SELECT * FROM manutencao")
    print(selectManutencao.fetchall())

    return cadastro
#endregion

#region ===REALIZAR MANUTENÇÃO===

def realiza_manutencao():
    print("\n-----REALIZAR MANUTENÇÃO-----")
    cpfPesquisa = int(input('\nDigite o CPF (apenas números) associados a manutenção que você deseja pesquisar: '))

    query = "SELECT COUNT() FROM manutencao WHERE cpf = {0}".format(cpfPesquisa)
    query = query.replace("[", "")
    query = query.replace("]", "")
    query = query.replace("(", "")
    query = query.replace(")", "")
    query = query.replace(",", "")

    conn.execute(query)
    print(query.fetchall())
    
    conn.commit() 
#endregion === FIM REALIZAR MANUTENÇÃO ===

#region ===MENU PRINCIPAL===
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
        #elif(opcao == 2):
        #   altera_manutencao()
        elif(opcao == 3):
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

#endregion