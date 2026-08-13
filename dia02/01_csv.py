# %%
import pandas as pd

# importando arquivos e lendo
df = pd.read_csv("../data/clientes.csv", sep=';')
df

# %%
# salvando arquivo sem o indice
df.to_csv("clientes.csv", index=False)

# %%
# arquivo binario
df.to_parquet("clientes.parquet", index=False)

# %%
df_2 = pd.read_parquet("clientes.parquet")
df_2

# %%
df.to_excel("clientes.xlsx", index=False)
df_3 = pd.read_excel("clientes.xlsx")
df_3