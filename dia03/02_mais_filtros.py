# %%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep=";")
df

# %%
filtro = (df["IdProduto"] == "5") | (df["IdProduto"] == "11")
df[filtro].head()

# %%
# usando a mesma logica acima utilizando o isin
filtro = df["IdProduto"].isin(["5", "11"])
df[filtro].head()

# %%
# filtrando NaN
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# clientes["DtCriacao"].notna()

filtro = clientes["DtCriacao"].isna()
clientes[filtro]

# %%
# fazendo a negação da condição
# essas duas linhas tem o mesmo resultado
~clientes["DtCriacao"].isna()
clientes["DtCriacao"].notna()