from database.createTables import *

def update_function(status, option, arg):
    #print(status, option, arg)
    conn.execute('''
                UPDATE manutencao
                set status = '{0}'
                WHERE {1} = "{2}"
                '''.format(status, option, arg))
    conn.commit()
    
    return print('Manutenção atualiza para status = "{0}"'.format(status))
