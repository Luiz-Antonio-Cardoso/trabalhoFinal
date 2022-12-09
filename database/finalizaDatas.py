from database.createTables import *
from datetime import datetime
from datetime import date

import sys
sys.path.append('./')

def finaliza_data(id):
    

    # for a in query.fetchall():
    #     dataInicio = a[0]
    #     dataFinal = a[1]

    # dataInicialSplitada = dataInicio.split('-')  
    # dataFinalSplitada = dataFinal.split('-')

    # print(dataInicialSplitada)

    
    dataSaida = date.today()

    dataSaida = str(dataSaida)
    dataSaida = dataSaida.split('-')
    dataSaida = dataSaida[2] + '/' + dataSaida[1] + '/' + dataSaida[0]

    date_format = "%d/%m/%Y"

    query = conn.execute('''SELECT dataEntrada FROM manutencao WHERE id = {0}'''.format(id))

    # for a in query.fetchall():
    #     dataInicial = a[0]

    dataInicial = query.fetchone()[0]

    dataInicio = datetime.strptime(dataInicial, date_format)
    dataFinal = datetime.strptime(dataSaida, date_format)
    diferenca = abs((dataFinal - dataInicio).days)
    
    return print('A manutenção {0} está foi finalizada com sucesso!!! Ela durou cerca de {1} dias'.format(id, (diferenca)))
