# %%
import pandas as pd

"""Exercício 1: Criação de Colunas com Operações Vetorizadas
O maior "superpoder" das estruturas do Pandas é a vetorização, que permite realizar cálculos em toda uma coluna sem usar laços for.
Tarefa:
1) Crie um DataFrame chamado df_produtos com as colunas produto, preço_unitario e quantidade.
2) Desafio: Crie uma nova coluna chamada valor_total que seja o resultado da multiplicação entre preço_unitario e quantidade.
3) Crie uma coluna chamada preço_com_taxa que adicione uma taxa fixa de 5.00 ao preço_unitario."""

# 1)
df_produtos = pd.read_csv("../data/transacao_produto.csv", sep=";")

df_produtos

# %%
# 2)
df_produtos["valor_total"] = df_produtos["QtdeProduto"] * df_produtos["vlProduto"]
df_produtos

# %%
# 3)
df_produtos["preço_com_taxa"] = df_produtos["vlProduto"] + 5
df_produtos

# %%
"""Exercício 2: Ordenação por Valores (sort_values)
Conforme vimos em nossa conversa anterior, a ordenação é fundamental para análise, mas exige atenção para saber se a mudança foi salva na variável.
Tarefa:
1) Utilizando o DataFrame do exercício anterior, ordene os dados pela coluna valor_total de forma decrescente (do maior para o menor).
2) Desafio: Como você faria para que essa ordenação fosse salva no DataFrame original sem precisar usar a atribuição df = df.sort_values(...)? (Dica: lembre-se do parâmetro que usamos no método .rename()).
3) Tente ordenar o DataFrame por duas colunas ao mesmo tempo: primeiro por quantidade (crescente) e depois por preço_unitario (decrescente)."""

# 1)
df_produtos.sort_values(by="valor_total", ascending=False)

# %%
# 2)
df_produtos.sort_values(by="valor_total", ascending=False, inplace=True)
df_produtos

# %%
# 3)
df_produtos.sort_values(by=["QtdeProduto", "vlProduto"], ascending=[True, False])

# %%
"""Exercício 3: Análise com Contagem e Ordenação
Muitas vezes, criar uma nova coluna envolve transformar dados existentes ou contar ocorrências para gerar insights.
Tarefa:
1) Adicione uma coluna chamada categoria ao seu DataFrame (ex: 'Eletrônico', 'Alimento', etc.).
2) Use o método .value_counts() para descobrir qual categoria aparece mais vezes no seu conjunto de dados.
3) Desafio de Ordenação: Após gerar a contagem de categorias, o resultado será uma Series. Como você ordenaria essa Series de contagem pelos nomes das categorias (em ordem alfabética) em vez de ordenar pelos valores numéricos?"""

# 1)
df_produtos["categoria"] = "Eletrônico"

# %%
# 2)
df_produtos["categoria"].value_counts()