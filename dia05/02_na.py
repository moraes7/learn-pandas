# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%
# remover todas as linhas que tem NA, NaN
# remover linhas que tem AO MENOS um NA
# dropna traz uma VIEW, mas como normalmente reatribuimos, nao sera mais uma view
clientes.dropna()

# %%
# definindo regras para o dropna
# o criterio de how="all" é que a LINHA INTEIRA seja NA para poder dropar
clientes.dropna(how="all")

# %%
# o default é how="any", ou seja, se encontrar ao menos UM NA, ele vai dropar
clientes.dropna(how="any")

# %%
# dataframe de brinquero para praticar
df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio", None],
        "idade": [None, None, 43, 52, 57],
        "salario": [3453, 4324, None, 5423, 1800]
    }
)
df
# %%
# removendo qualquer NA que encontrar
df.dropna()

# %%
# remove somente quando a linha inteira for NA
df.dropna(how="all")

# %%
# remove somente quando a IDADE for NA
df.dropna(how="all", subset=["idade"])

# %%
# remover somente quando a linha inteira de IDADE e SALARIO for NA
df.dropna(how="all", subset=["idade", "salario"])

# %%
# remover quando tiver ao minimo um NA
df.dropna(how="any", subset=["idade", "salario"])

# %%
# fillna é uma maneira de completar os valores, os preenchendo, substituindo a CÉLULA
df["idade"] = df["idade"].fillna(0)

# %%
# o "alguem" vai completar todas as celulas de nome que estao NA, como no caso tem 2 celulas nome NA, terao 2 "alguem" 
df.fillna(
    {
        "nome": "alguem",
        "idade": 0
    }
)

# %%
# media de idade e salario com fillna
medias = df[["idade", "salario"]].mean()
df.fillna(medias)