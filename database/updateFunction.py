from database.createTables import *

#status => F = Finalizado, A = Aberto, C = Cancelado, M = Manutenção
#option => vai ser o campo que vai ser usado para como chave para alteração
#arg => vai ser o valor do campo atualizado
def update_function(status, option, arg):
    #print(status, option, arg)
    conn.execute('''
                UPDATE manutencao
                set status = '{0}'
                WHERE {1} = "{2}"
                '''.format(status, option, arg))
    conn.commit()
    
    return print('Manutenção atualiza para status = "{0}"'.format(status))
