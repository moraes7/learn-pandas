# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%
# ordenando uma SERIE de forma crescente em quantidade de pontos
clientes["qtdePontos"].sort_values()

# %%
# buscando o maior numero de pontos
max_pontos = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_pontos
clientes[filtro]

# %%
# ordenando um DATAFRAME de forma crescente em quantidade de pontos
clientes.sort_values(by="qtdePontos").head(5)
# %%
# ordenando um DATAFRAME de forma decrescente em quantidade de pontos
clientes.sort_values(by="qtdePontos", ascending=False).head(5)

# %%
# buscando apenas pelo id do cliente que mais tem pontos
top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
         .head(5)["idCliente"] )
top_5

# %%
# o arquivo clientes não está sofrendo alteração, porque o sort_values retorna um dataframe NOVO
clientes

# %%
# caso houvesse empate dos pontos
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario": [2345, 4533, 3245, 4533]
    }
)
brinquedo

# %%
# ordenando pelo salário e pela idade, caso o salário de empate a idade será o critério de desempate
brinquedo.sort_values(by=["salario", "idade"], ascending=False)

# %%
# ordenando com um sendo ascendente e outro descendente 
brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])