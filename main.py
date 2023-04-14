import requests
import pandas as pd
import json


# No lugar desta etapa coloque seus dados no lugar das variaveis
with open('credenciais.json', 'r') as f:

    dados = json.load(f)

usuario = dados["login"]
senha = dados["senha"]
url_login = dados["url_login"]
url_teste = dados["url_teste"]



# Realize o login na API
def login():

    header = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    body = {
        '_username': usuario,
        '_password': senha
    }

    myResponse = requests.post(url_login, data=body, headers=header)

    resposta = myResponse.json()

    token = resposta["token"]


    return token

# Agora prepare os dados de uma forma que fique facil de manipular no Power Query
def extract_data_dfranquias(token, urls):

    df = pd.DataFrame()

    for nome_tbl in urls:
        
        url = urls[nome_tbl]

        header = {
            'Authorization': 'Bearer ' + token
        }
    
        myResponse = requests.get(url, headers=header)

        my_string = myResponse.content.decode('utf-8')

        data = json.loads ( my_string )

        # retorne um dataframe com o resultado obtido

        df = pd.DataFrame( data )


    return df


tabelas = {"teste": url_teste}

# defina o valor em uma variavel e print o valor
df = extract_data_dfranquias(login(), tabelas)['items']

print(df)