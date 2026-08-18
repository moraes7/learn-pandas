# %%
import pandas as pd

df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["teo", "jose", "nah", "mah", "lah"],
})

df_02 = pd.DataFrame({
    "cliente": [6,7,8],
    "nome": ["kozato", "laura", "dan"],
    "idade": [32,29,31],
})

df_03 = pd.DataFrame({
    "idade": [32,34,19,54,33],
})

# %%
# empilhando os dataframes
# concat = concatenar
# concat espera que voce passe uma lista de dataframes
# ignore_index=True reseta o index que mateve dos dataframes

dfs = [df, df_02]

pd.concat(dfs, ignore_index=True)

# %%

df_03 = df_03.sort_values(by="idade").reset_index(drop=True)
df_03
# %%
# definir como concatenar os dataframes
# podemos escolher se queremos concatenar de cima para baixo ou da esquerda para direita
pd.concat([df, df_03], axis=1)