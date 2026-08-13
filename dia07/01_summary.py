# %%
import pandas as pd

idades = [32, 44, 12, 54, 67, 32, 23, 34, 32, 12, 45, 43, 28, 73, 29]
idades = pd.Series(idades)
idades

# %%
# a estatística de um conjunto de dados nada mais é que representar esse conjunto de dados a partir de um ÚNICO valor

# soma de todas as idades
int(idades.sum())

# buscando a menor idade
int(idades.min())

# buscando a maior idade
int(idades.max())

# média das idades
int(idades.mean())

# lista de estatísticas
idades.describe()

# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%
int(clientes["flTwitch"].sum())
clientes["flTwitch"].mean()

# %%
# todas as redes sociais
# se aplicamos a média em uma SERIE, será retornado uma agregação daquela SERIE
# se aplicarmos a média em um DATAFRAME, será aplicado a média em cada uma das colunas do DATAFRAME
redes_sociais = ["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]
clientes[redes_sociais].mean()

# %%
# buscando apenas um unico tipo na coluna
# object
clientes.dtypes[clientes.dtypes == "object"].index.tolist()

# buscando colunas do tipo numérico
clientes.dtypes[~(clientes.dtypes == "object")].index.tolist()

# %%
# mean() calcula um único valor por coluna (a média). Como resultado, pra cada coluna você tem só 1 número — e isso é exatamente a estrutura de uma Series: índice = nome da coluna, valor = a média.

# describe() calcula várias estatísticas por coluna (count, mean, std, min, 25%, 50%, 75%, max — geralmente 8 valores). Como cada coluna agora tem múltiplos valores associados, o pandas precisa de uma estrutura bidimensional pra organizar isso: as colunas continuam sendo as colunas originais, mas as linhas viram os nomes das estatísticas (count, mean, std...). Isso é exatamente o formato de um DataFrame.

# O mean() pega o DataFrame e devolve uma linha só com um número por coluna — por isso vira Series
# Já o describe() calcula várias estatísticas (count, mean, std, min, 25%...) para cada coluna — então ele monta uma tabelinha: as colunas continuam sendo as originais, e as linhas viram os nomes das estatísticas. Isso já é bidimensional, por isso vira DataFrame 

# A regra prática que dá pra levar pra qualquer método do pandas: se o resultado é 1 valor por coluna → Series. Se é vários valores por coluna organizados numa tabela → DataFrame

num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.tolist()
clientes[num_columns].mean()
clientes[num_columns].describe()

# %%
# RESUMINDO:

# UMA ÚNICA COLUNA RETORNA APENAS UM NÚMERO
clientes["flTwitch"].mean()

# MAIS DE UMA COLUNA RETORNA UMA SERIE
clientes[["flTwitch", "flYouTube"]].mean()

# UMA COLUNA COM UM DESCRIBE JÁ RETORNA UMA SERIE
clientes["flTwitch"].describe()

# MAIS DE UMA COLUNA COM UM DESCRIBE RETORNA UM DATAFRAME, PORQUE É MAIS DE UMA ÚNICA SERIE
# LEMBRE-SE QUE O "VARAL" DE UMA SERIE É UM DATAFRAME
clientes[["flTwitch", "flYouTube"]].describe()
