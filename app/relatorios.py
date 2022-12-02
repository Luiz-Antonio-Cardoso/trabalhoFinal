import sys

from utilities.relatorios import relatorios
sys.path.append('./')
from utilities.Menu import menu
#from app.relatorios import relatorios

def gerarRelatorios():
    opcoes_menu = [
        'Relatório geral'
        'Relatório manutenção tipo A', 
        'Relatório manutenção tipo M', 
        'Relatório manutenção tipo C', 
        'Relatório manutenção tipo F', 
        'Relatório total recebido', 
        'Relatório de manutenções por CPF'
        ] 
    nome = 'RELATÓRIOS'
    opcao = menu(opcoes_menu, nome)
    
    if (opcao == 1):
         relatorios()
    elif (opcao == 2):
        relatorios('WHERE status = "A"')
    elif (opcao == 3):
        relatorios('WHERE status = "M"')
    elif (opcao == 4):
        relatorios('WHERE status = "C"')
    elif(opcao == 5):
        relatorios('WHERE status = "F"')
    elif(opcao == 6):
        relatorios('WHERE status = "F"')
    elif (opcao == 7):
        cpfPesquisa = menu([], 'RELATÓRIOS', 'Digite o CPF (apenas números) associados a manutenção que você deseja pesquisar: ')
        where = 'WHERE cpf = {0}'.format(cpfPesquisa)
        print(where)
        relatorios(where)
    else:
        print('\n\nOpção inválida, por favor digite uma opção verdadeira.\n\n')

