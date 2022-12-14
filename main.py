# imports
from app.alterarManutencao import altera_manutencao
from app.cadastroManutencao import cadastro_manutencao 
from app.finalizarManutencao import finaliza_manutencao
from app.realizarManutencao import  realiza_manutencao 
from app.gerarRelatorios import gerarRelatorios
from utilities.Menu import menu

from database.createTables import criarTabela

#criarTabela()

def menu_principal():   

    op = True
    while op == True:
        
        opcoes_menu = ['Cadastrar manutenção', 'Alterar manutenção', 'Realizar manutenção', 'Finalizar manutenção', 'Relatórios', 'Sair']
        nome = "MENU PRINCIPAL"
        opcao = int(menu(opcoes_menu, nome))

        if (opcao == 1):
            cadastro_manutencao()
        elif (opcao == 2):
            altera_manutencao()
        elif (opcao == 3):
            realiza_manutencao()
        elif(opcao == 4):
            finaliza_manutencao()
        elif(opcao == 5):
            gerarRelatorios()
        elif (opcao == 6):
            print('Saindo...')
            op = False
        else:
            print('\n\nOpção inválida, por favor digite uma opção verdadeira.\n\n')


menu_principal()