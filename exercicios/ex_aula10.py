# %%
# selecione a primeira transação diária de cada cliente:
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# 1) ordenar
transacoes = transacoes.sort_values("DtCriacao")

# 2) criar uma data para transicao
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date

# 3) deduplicar data com idcliente para pegar apenas a primeira transicao do dia
transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])