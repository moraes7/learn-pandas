# %%
import pandas as pd

# %%

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")
transacao_produto.head()

produtos = pd.read_csv("../data/produtos.csv", sep=";")
produtos.head()
# %%
produtos.head()
# %%
cliente_transacao_produto = transacoes.merge(
    transacao_produto,
    on="IdTransacao",
    how="left"
)[["IdTransacao", "IdCliente", "IdProduto"]]

df_full = cliente_transacao_produto.merge(
    produtos,
    on=["IdProduto"],
    how="left"
)

df_full = df_full[df_full["DescNomeProduto"] == "Presença Streak"]

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
        .count()
        .sort_values(ascending=False)
        .head(1)
)

# %%
# maneira mais avançada e performatica

produtos = produtos[produtos["DescNomeProduto"] == "Presença Streak"]

(transacoes.merge(transacao_produto, on="IdTransacao", how="left")
           .merge(produtos, on=["IdProduto"], how="right")
           .groupby(by="IdCliente")["IdTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(1)
)
