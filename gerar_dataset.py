from faker import Faker
import numpy as np
import pandas as pd

def gerar_dataset(numero_clientes: int):
    """ Função gerar_dataset cria um arquivo csv com as seguintes informações:
    id_cliente, 
    idade (18~65),
    renda_mensal (1518 ~ 20000),
    tempo_contas_meses (1 ~ 60 meses)
    uso_cartao (quantidade de uso de cartão)
    uso_pix   (quantidade de pix)
    solicitou_emprestimo (solicitou pix? 1 = sim , 0 = não)
    churn (1 ou 0)
    """
    fake = Faker()
    np.random.seed(42)

    num_clientes = numero_clientes
    dados =  {
        "id_cliente": [fake.uuid4() for _ in range(num_clientes)],
        "idade": np.random.randint(18,65,num_clientes),
        "renda_mensal": np.random.randint(1518,20000, num_clientes),
        "tempo_conta_meses": np.random.randint(1,60,num_clientes),
        "uso_cartao": np.random.randint(0,50,num_clientes),
        "uso_pix": np.random.randint(0,100,num_clientes),
        "solicitou_emprestimo": np.random.choice([0,1], num_clientes, p=[0.8,0.2]),
        "churn": np.random.choice([0,1], num_clientes, p=[0.7,0.3])

    }

    df_nubank  = pd.DataFrame(dados)
    df_nubank.to_csv("dataset/churn_nubank.csv", index=False)


if __name__ == '__main__':
    gerar_dataset(1000)
