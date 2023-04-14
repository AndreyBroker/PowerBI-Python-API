# Conectar o Power BI a uma API Rest com token JWT

## Requisitos: Python e Power BI

### Instalação do python: https://www.python.org/

### Obs: Antes de realizar as entapas, prepare seu código python seguindo as orientações do arquivo "main.py". Além disso, cetifique que as bibilotecas "pandas" e "requests" estão instaladas no pip realizando o comando "pip show pandas requests". Caso não estaje realize o comando pip install requests e pip install pandas.

## 1 - Primeiro Passo
#### Abra o Power query.
![alt text](./imagens_pbi/1.png)

## 2 - Segundo Passo
#### Clique em Nova Fonte (Canto Superior esquerdo), seguida clique em mais.
<img src="./imagens_pbi/2.png" width="350">

## 3 - Terceiro Passo
#### Pesquise por "Script do Python" e clique na opção.
<img src="./imagens_pbi/3.png" width="350">

## 4 - Quarto Passo
#### Copie e Cole o Script python criado anteriormente e clique em ok.
<img src="./imagens_pbi/4.png" width="350">

## Final
### Agora finalmente os dados da API não retornados!
<img src="./imagens_pbi/5.png" width="350">

## Problemas
### Caso retorne vazio, tente rodar o programa no VSCode testando para ver se está tudo certo, caso o erro persista, tente retorna a API pura, sem realizar tratamentos no python.