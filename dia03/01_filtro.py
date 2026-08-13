# %%
import pandas as pd

# %%
# filtrando transaçoes com mais de 50 pts sem pandas
pontos = [10, 1, 1, 1, 50, 100, 130, 1, 1, 30, 25, 50]
filtro = []

for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado

# %%
# filtrando quem tem mais de 18 anos usando pandas
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32, 35, 14],
        "uf": ["sp", "pr", "rj"]
    }
)

filtro = brinquedo["idade"] >= 18

brinquedo[filtro]

# %%
# filtrando qtd de pontos maior ou igual a 50
df = pd.read_csv("../data/transacoes.csv", sep=";")

filtro = df["QtdePontos"] >= 50
df[filtro].head(n = 10)

# %%
# filtrando qtd de pontos maior e igual a 50 e menor do que 100
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filtro].sample(10)

# %%
# filtrando qtd de pontos igual a 1 ou igual a 100
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro].sample(50)

# %%
# filtrando pontos entre 0 a 50 ou do ano 2025 para frente
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) | (df["DtCriacao"] >= "2025-01-01")
df[filtro].sample(10)