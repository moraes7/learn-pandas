# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=';')
df

# %%
df.shape

# %%
df.info(memory_usage='deep')

# %%
df.dtypes

# %%
# renomeando nome das colunas
renamed_columns = {
    "QtdePontos": "QtdPontos",
    "DescSistemaOrigem": "SistemaOrigem"
}
# df = df.rename(renamed_columns)
# alterando sem precisar reatribuir o df
df.rename(columns=renamed_columns, inplace=True)
df

# %%
# quando passamos uma lista é retornado um dataframe com 1 ou mais colunas
# com apenas UMA chave é retornado uma serie, agora com uma lista de chaves é retornado um dataframe
# df[["IdCliente", "QtdPontos", "DtCriacao"]]
# maneira com melhor legibilidade:
colunas = ["IdCliente", "QtdPontos", "DtCriacao"]
df[colunas]

# %%
# COMPARAÇÕES DE PANDAS COM SQL

# SELECT * FROM df
df

# %%
# SELECT IdCliente FROM df
df[["IdCliente"]]

# %%
# SELECT IdCliente, QtdPontos FROM df LIMIT 5
# sample é util para verificar a consistencia dos dados em diferentes partes do dataset de forma imparcial
df[["IdCliente", "QtdPontos"]].sample(5)

# %% 
# MUDANDO A ORDEM 
# SELECT IdCliente, IdTransacao, QtdPontos FROM df LIMIT 5
df[["IdCliente", "IdTransacao", "QtdPontos"]].head(5)

# %%
# ORDENANDO EM ORDEM ALFABETICA
colunas = list(df.columns)
colunas.sort()
colunas

# podemos reordenar as colunas definindo a lista e ordem que queremos, e depois reatribuimos para o df
df = df[colunas]
df