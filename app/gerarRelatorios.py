import sys
sys.path.append('./')
#copilot import the relatorios function from reports
from app.reports.relatorios import relatorios

from utilities.Menu import menu
#from app.relatorios import relatorios

def gerarRelatorios():
    opcoes_menu = [
        'Relatório geral',
        'Relatório manutenção tipo A', 
        'Relatório manutenção tipo M', 
        'Relatório manutenção tipo C', 
        'Relatório manutenção tipo F', 
        'Relatório total recebido', 
        'Relatório de manutenções por CPF'
        ] 
    nome = 'RELATÓRIOS'
    opcao = int(menu(opcoes_menu, nome))
    
    #para cada opção, chama a função relatorios com os parâmetros adequados
    #a função relatorios está no arquivo relatorios.py
    #ela recebe dois parâmetros: o que deve ser selecionado e o filtro
    #se o filtro for vazio, não é necessário passar o segundo parâmetro
    if (opcao == 1):
         relatorios('*')
    elif (opcao == 2):
        relatorios('*', 'WHERE status = "A"')
    elif (opcao == 3):
        relatorios('*', 'WHERE status = "M"')
    elif (opcao == 4):
        relatorios('*', 'WHERE status = "C"')
    elif(opcao == 5):
        relatorios('*', 'WHERE status = "F"')
    elif(opcao == 6):
        #vai retornar a soma de todos os valores de manutenções
        relatorios('SUM(valor)', 'WHERE status = "M"')
    elif (opcao == 7):
        #vai retornar um relatório baseado no cpf digitado
        cpfPesquisa = menu([], 'RELATÓRIOS', 'Digite o CPF (apenas números) associados a manutenção que você deseja pesquisar: ')
        relatorios('*', 'WHERE cpf = "{0}"'.format(cpfPesquisa))
    else:
        print('\n\nOpção inválida, por favor digite uma opção verdadeira.\n\n')

