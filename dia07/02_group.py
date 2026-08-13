# %%
# Quem teve mais transações de Streak?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
# contar e agrupar quantidades de cada cliente
# todas as colunas
transacoes.groupby(by=["IdCliente"]).count().head()

# %%
# contar apenas a quantidade de transações
# retorna uma serie onde o indice é o id do cliente e os valores sao a quantidade de transações que o cliente fez
transacoes.groupby(by=["IdCliente"])["IdTransacao"].count().head()

# %%
# retornar um dataframe inves de uma serie
transacoes.groupby(by=["IdCliente"])[["IdTransacao"]].count().head()

# %%
# caso queira que o id fique como uma coluna e nao um indice
transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count().head()

# %%
# quantidade de pontos
# calcular a soma de pontos que cada pessoa juntou
# calcular a media de pontos por transação
summary = (transacoes.groupby(by=["IdCliente"], as_index=False)["QtdePontos"]
                     .agg({"IdTransacao": ['count'],
                           "QtdePontos": ['sum', 'mean']}))

summary

# %%
# esse dataframe é um tipo de multi index (hierarquia nas colunas)
summary.columns

# %%
# acessando um valor multi index
summary[("QtdePontos", "mean")]

# %%
# tornando essa hierarquia chata um pouco mais acessível
# definindo a coluna nós mesmos
# com isso acaba o multi index
summary.columns = ["IdCliente", "qtdeTransacao", "totalPontos", "media"]
summary

# %%
