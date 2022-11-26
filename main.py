# imports

from app.facade import *
from database.createTables import criarTabela
from utilities.facade import *

criarTabela()

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
        elif(opcao == 4):
          finaliza_manutencao()
        elif(opcao == 5):
          relatorios()
        elif (opcao == 6):
            sair()
        else:
            print('\n\nOpção inválida, por favor digite uma opção verdadeira.\n\n')


menu_principal()
