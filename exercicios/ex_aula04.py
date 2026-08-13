# %%
import pandas as pd

"""Exercício 1: Inspeção e Dimensões
Neste exercício, vamos focar em como ter uma "visão geral" do seu conjunto de dados assim que ele é importado
Tarefa:
1) Importe um arquivo CSV fictício chamado vendas.csv para um DataFrame chamado df_vendas
2) Como você faria para visualizar apenas as 7 primeiras linhas do conjunto?
3) E para ver as 3 últimas linhas?
4) Verifique as dimensões do seu DataFrame (total de linhas e colunas) sem usar uma função (usando um atributo)
5) Desafio: Como você pegaria uma amostra aleatória de 5 linhas para garantir que os dados não estão viciados em uma ordem específica?"""

# 1)
df_produtos = pd.read_csv("data/produtos.csv", sep=';')
df_produtos

# %%
# 2)
df_produtos.head(n = 7)

# %%
# 3)
df_produtos.tail(n = 3)

# %%
# 4)
df_produtos.shape

# %%
# 5)
df_produtos.sample(5)

# %%
"""Exercício 2: Metadados e Tipagem
O objetivo aqui é entender a estrutura técnica dos dados (tipos de colunas e uso de memória)
Tarefa:
1) Use o método que exibe um resumo completo do DataFrame, incluindo valores não nulos e tipos de dados
2) O atributo .dtypes retorna uma estrutura do Pandas. Que estrutura é essa (Series ou DataFrame)?
3) Acesse apenas os nomes das colunas do seu DataFrame
4) Desafio: Imagine que você tem uma coluna chamada data_venda. Como você usaria o atributo .dtypes para descobrir especificamente o tipo de dado dessa coluna?"""

# 1)
df_produtos.info()

# %%
# 2) É uma Series
df_produtos.dtypes

# %%
# 3)
colunas = list(df_produtos.columns)
colunas
# %%
# 4)
df_produtos["IdProduto"].dtypes

# %%
"""Exercício 3: Renomeação e Seleção de Colunas
Aqui você vai praticar a alteração e a seleção seletiva de dados, comparando com a lógica do SQL
Tarefa:
1) Renomeie a coluna valor_total para receita e id_cliente para cliente_id usando um dicionário. Faça isso de forma que a alteração seja salva no próprio DataFrame original (sem precisar reatribuir a variável)
2) Selecione apenas as colunas cliente_id e receita, mas garanta que o resultado retornado seja um DataFrame e não uma Series
3) Desafio de Reordenação: Como você faria para exibir o DataFrame com as colunas em ordem alfabética automaticamente, sem precisar digitar nome por nome?
"""

# 1)
renamed_columns = {
    "DescNomeProduto": "NomeProduto",
    "DescDescricaoProduto": "DescricaoProduto"
}

df_produtos.rename(columns=renamed_columns, inplace=True)
df_produtos

# %%
# 2)
colunas = ["NomeProduto", "DescricaoProduto"]
df_produtos[colunas]

# %%
# 3)
ordem_alfabetica = list(df_produtos.columns)
ordem_alfabetica.sort()
ordem_alfabetica

df_produtos = df_produtos[ordem_alfabetica]
df_produtos

# %%
df_produtos.columns