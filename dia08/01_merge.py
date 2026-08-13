# %%
import pandas as pd

# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %%
# juntando as informações de duas colunas criando uma base com transações e as informações do cliente 
# podemos partir da base que queremos
#  na época que o Téo fez o curso nas duas tabelas o nome era o mesmo ["IdCliente"], no kaggle atual elas estão com nomes diferentes. Então tem que usar o  left_on= ["IdCliente"], right_on= ["idCliente"])
# codigo da epoca: right=clientes, how="left", on["idCliente"]
# colunas repetidas ficam _x/_y, para isso se usa suffixes

transacoes.merge(
    right=clientes, 
    left_on=["IdCliente"], 
    right_on=["idCliente"],
    how="left",
    suffixes=["Transação", "Cliente"]
).head()

# %%
# brinquedo

df_1 = pd.DataFrame({
    "transacao": [1,2,3,4,5],
    "idCliente": [1,2,3,2,2],
    "valor": [10,45,32,17,87],
})

df_2 = pd.DataFrame({
    "id": [1,2,3,4],
    "nome": ["teo", "nah", "mah", "jose"],
})

df_1.merge(
    df_2, 
    left_on=["idCliente"], right_on=["id"],
    how="left"
)