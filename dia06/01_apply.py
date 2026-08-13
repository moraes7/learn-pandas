# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%
#  podemos criar métodos personalizados e aplicar no dataframe utilizando método apply (sem precisar percorrer uma lista de valores com for por exemplo)
# pegando a apenas a última parte do ID do cliente
def get_last_id(id):
    return id.split("-")[-1]

get_last_id("001ebba5-5491-400a-ad05-d9204ea11cca")

# %%
# forma arcaica
id_novo = []

for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["NovoId"] = id_novo
df.head()

# %%
# no lugar de fazer tudo isso que fizemos antes, existe o APPLY

dataframe = df["idCliente"].apply(get_last_id)
dataframe.head()