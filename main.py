import requests
import pandas as pd
import json


# Coloque aqui suas informações

usuario = "teste@gmail.com"
senha = "12345"
url_login = "https://api.login.com"
url_teste = "https://api.teste.com"



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
df = extract_data_dfranquias(login(), tabelas)

print(df)