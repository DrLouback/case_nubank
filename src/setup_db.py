import psycopg2
import os
from dotenv import load_dotenv

def create_tables():
    """ Cria a tabela de clientes e transacoes: 

    create_table_query = CREATE TABLE IF NOT EXISTS clientes (
        id_cliente UUID PRIMARY KEY,
        idade INT,
        renda_mensal DECIMAL(10,2),
        tempo_conta_meses INT
        );

        CREATE TABLE IF NOT EXISTS transacoes (
        id_transacao SERIAL PRIMARY KEY,
        id_cliente UUID REFERENCES clientes(id_cliente),
        uso_cartao INT,
        uso_pix INT,
        solicitou_emprestimo BOOLEAN,
        churn BOOLEAN
        );            
    """
    load_dotenv()
    DATABASE_URL = os.getenv('DATABASE_URL')

    try:

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        create_table_query = """ CREATE TABLE IF NOT EXISTS clientes (
        id_cliente UUID PRIMARY KEY,
        idade INT,
        renda_mensal DECIMAL(10,2),
        tempo_conta_meses INT
        );

        CREATE TABLE IF NOT EXISTS transacoes (
        id_transacao SERIAL PRIMARY KEY,
        id_cliente UUID REFERENCES clientes(id_cliente),
        uso_cartao INT,
        uso_pix INT,
        solicitou_emprestimo INT,
        churn INT
        );
                            """
        
        cursor.execute(create_table_query)
        conn.commit()

        print('Tabela criada com sucesso!')

    except Exception as e:
        raise Exception(f'Ocorreu um erro: {e}')

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    create_tables()