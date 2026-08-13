# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df["qtdePontos"]

# %%
# convertendo o tipo da serie para outro tipo
# astype retorna a serie
df["qtdePontos"].astype(float).astype(str)

# %%
# substituindo um valor
# lembrando que isso nao substitui o valor original, é retornado uma NOVA serie
df["DtCriacao"].replace({
    "0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"
})

# %%
# para reatribuir o valor
# O replace substitui o valor inteiro da célula por outro
df["DtCriacao"] = df["DtCriacao"].replace({
    "0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"
})

# %%
# convertendo para data
pd.to_datetime(df["DtCriacao"])

# %%
# uma forma mais otimizada e mais comum
replace = {"0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"}

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))
df["DtCriacao"]

# %%
# acessando datas
df["DtCriacao"].dt.year
df["DtCriacao"].dt.day
df["DtCriacao"].dt.month
df["DtCriacao"].dt.month_name()
df["DtCriacao"].dt.day_of_week
df["DtCriacao"].dt.date