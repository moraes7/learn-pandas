# %%
import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
# criando um metodo para calcular a amplitude, calcular a distancia dessa altitude para a media, elevar ao quadrado e tirar a raiz

def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude-media)**2)

# %%
# tempo de vida do usuario
def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days

# %%
# entao, podemos criar metodos personalizados para fazer um groupby(agregação)
# sendo assim muito customizável

summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
           .agg({
               "IdTransacao": ["count"],
               "QtdePontos": ["sum", "mean", diff_amp],
               "DtCriacao": [life_time]
           })
)

summary.columns = [
    "IdCliente",
    "QtdeTransacao",
    "total_pontos", 
    "media_pontos",
    "ampMeanDif",
    "lifeTime",
]
summary.head()