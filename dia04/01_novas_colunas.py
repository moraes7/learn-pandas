# %%
import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%
nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append(i+100)
nova_coluna

# %%
# invés de usarmos o for, a serie já permite fazermos uma operação matematica com um escalar, aplicando essa operação para cada elemento dentro dela
# é mais rápido e otimizado do que o for
df["qtdePontos"] + 100

# %%
# criando uma nova coluna
df["pontos_100"] = df["qtdePontos"] + 100
df.sample(n = 5)

# %%
# saber se um cliente tem pelo menos email ou twitch, se tiver os dois o resultado é 2, não é uma operação booleana true ou false
# as series tem que ter a mesma dimensão(mesmo tamanho, mesma quantidades de elementos)
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%
# saber se o cliente pelo menos um email ou twitch
df["flEmail"] * df["flTwitch"]

# somar para saber quantas redes sociais um cliente tem
df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head()

# %%
# saber se o cliente tem todas as redes sociais
df["todas_social"] = df["qtdeSocial"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df

# %%
df["qtdePontos"].describe()

# %%
# usando numpy para aplicar um logaritmo
# o numpy será usado em funções matemáticas que precisar transformar dados
# usar +1 para evitar -inf(infinitos)
# melhora a distribuição
df["logPontos"] = np.log(df["qtdePontos"]+ 1)
df["logPontos"].describe()

# %%
import matplotlib.pyplot as plt
plt.hist(df["logPontos"])
plt.grid(True)
plt.show()