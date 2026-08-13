# %%
import pandas as pd

# %%
df = pd.DataFrame({
    "nome": ["teo", "lara", "nah", "bia", "mah", "lara", "mah", "mah"],
    "sobrenome": ["calvo", "calvo", "ataide", "ataide", "silva", "silva", "silva", "silva"],
    "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134]
})

df
# %%
# removendo duplicatas
# drop_duplicates() sempre manterá a primeira
df.drop_duplicates()

# %%
# escolhendo o que remover
# mantendo a ultima
# nao é possivel remover uma intermediária
df.drop_duplicates(keep="last")

# %%
# removendo duplicatas pelo nome e sobrenome
df.drop_duplicates(keep="last", subset=["nome", "sobrenome"])

# %%
# é importante ordernar o dataset, porque ate agora trabalhamos de forma arbitraria
# fazendo de uma forma comum e otimizada
df = (df.sort_values("salario", ascending=False)
      .drop_duplicates(keep="last", subset=["nome", "sobrenome"]))
df