import sqlite3

conn = sqlite3.connect("db-oficina")
cursor = conn.cursor()


def criarTabela():
    cursor.execute('''CREATE TABLE manutencao (
                    id INTEGER PRIMARY KEY NOT NULL,
                    nome NVARCHAR(50) NOT NULL,
                    cpf NVARCHAR(11) NOT NULL,
                    tipoVeiculo NVARCHAR (50),
                    detalhe NVARCHAR(200) NOT NULL,
                    valor FLOAT NOT NULL,
                    descricao NVARCHAR (200) NOT NULL,
                    dataEntrada DATE NOT NULL,
                    dataSaida DATE NOT NULL,
                    status NVARCHAR(1) NOT NULL
                  );''')
