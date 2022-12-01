import sys
sys.path.append('./')
from utilities.Menu import menu

def relatorios():
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
        relatorioGeral()
    elif (opcao == 2):
        relatorioStatusA()
    elif (opcao == 3):
        relatorioStatusM()
    elif (opcao == 4):
        relatorioStatusC()
    elif(opcao == 5):
        relatorioStatusF()
    elif(opcao == 6):
        relatorioTotal()
    elif (opcao == 7):
        relatorioCPF()
    else:
        print('\n\nOpção inválida, por favor digite uma opção verdadeira.\n\n')
