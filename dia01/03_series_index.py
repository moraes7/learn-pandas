# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

series_idades = pd.Series(idades)
series_idades

# %%
# acessando o primeiro elemento da lista
#idades[0]
int(series_idades[0])
# %%
series_idades = series_idades.sort_values()
series_idades

# %%
# acessando o valor 23 com indice 11 depois do sort
# com iloc nao usamos mais indice como chave e sim como posiçao
# iloc ignoramos o indice e buscando as linhas
int(series_idades.iloc[0])

# %%
# acessando a ultima posiçao
int(series_idades.iloc[-1])

# %%
# acessando os 3 primeiros valores com slice
series_idades.iloc[:3]

# do ultimo ate o primeiro
series_idades[::-1]

# %%
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

indexs = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

series_idades = pd.Series(idades, index=indexs)
series_idades

# %%
int(series_idades["Nih"])

# %%
int(series_idades.iloc[0])

# %%
series_idades["Kozato"]

# %% acessando o ultimo kozato
int(series_idades.iloc[-1])

# %% posiçao e index buscando por posiçao
series_idades.iloc[[-1]]

# %%
# loc é navegar nos indices, mas nas series nós ja navegamos diretamente nos indices, entao o loc pode ser ocultado (default)
# series_idades.loc["Mah"] == series_idades["Mah"] 
int(series_idades.loc["Mah"])