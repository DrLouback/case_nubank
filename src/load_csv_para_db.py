import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

try:
    #criação da conexão com o banco de dados
    DATABASE_URL = os.getenv('DATABASE_URL')
    engine = create_engine(f'{DATABASE_URL}')


    #Carregar o dataset criado com o Faker e carregar os dados no banco de dados
    dataset = pd.read_csv('dataset/churn_nubank.csv')

    dataset_clientes = dataset[['id_cliente','idade','renda_mensal','tempo_conta_meses']]
    dataset_clientes.to_sql("clientes", engine, if_exists='replace', index=False)


    dataset_transacoes = dataset[['id_cliente','uso_cartao','uso_pix','solicitou_emprestimo','churn']]
    dataset_transacoes.to_sql('transacoes', engine, if_exists='replace', index=False)

    print('Dados foram carregados com sucesso!')
except Exception as e:
    raise Exception(f'Ocorreu um erro: {e}')
