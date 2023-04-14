import requests
import pandas as pd
import json


usuario = "andreybroker02@gmail.com"
senha = "redeioa"
url_login = "https://api.dfranquias.com/v2/login_check"
url_teste = "https://api.dfranquias.com/v2/franquias?count=50"



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

    

        df = pd.DataFrame( data )


    return df


tabelas = {"teste": url_teste}

df = extract_data_dfranquias(login(), tabelas)

print(df)