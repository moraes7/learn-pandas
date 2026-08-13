# %%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes

# AMOSTRAS
# %%
# exibindo as 5 primeiras linhas do dataframe
df_clientes.head()

# %%
# exibindo uma quantidade maior que queremos
df_clientes.head(n=10)

# %%
# exibindo as ultimas linhas do dataframe
df_clientes.tail(10)

# %%
# exibindo sortidos(embaralhado)
df_clientes.sample(10)

# %%
# exibindo quantidade de linhas e colunas
# shape nao é um metodo, mas sim um atributo
# shape exibe uma tupla
df_clientes.shape

# %%
# exibindo o nome das colunas
df_clientes.columns

# %%
# exibindo os indices
df_clientes.index

# %%
# exibindo informaçoes do dataframe (formato em string)
df_clientes.info()
# exibindo o valor exato de memoria consumida
df_clientes.info(memory_usage='deep')

# %%
# exibindo uma serie que mostra os valores da tipagem de cada coluna
df_clientes.dtypes