# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.info()

# %%
# quando fazemos um filtro num dataframe, ele nao retorna uma cópia do dataframe anterior so com as linhas filtradas
# isso se chama VIEW
# o clientes_0 está apontando para as mesmas linhas que clientes, mas só para as linhas onde o filtro é verdadeiro
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro]
clientes_0["flag_1"] = 1
