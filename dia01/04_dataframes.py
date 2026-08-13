# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

nomes = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%
# dataframe é um varal onde penduramos series nele
# uma serie é como se fosse uma coluna da planilha excel
# um dataframe é a planilha como um todo
df = pd.DataFrame()
df["Nomes"] = nomes
df["Idades"] = idades
df

# %%
# navegando pela planilha
df["Idades"]

# %%
# buscar todas as informaçoes de uma linha especifica
df.iloc[3]
df.iloc[11]["Nomes"]
int(df.iloc[0]["Idades"])
df.mean()