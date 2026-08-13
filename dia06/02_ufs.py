# %%
import pandas as pd
import requests
from io import StringIO

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

dfs = pd.read_html(StringIO(response.text))

uf = dfs[1]

# %%
# estao em int: Densidade (2005), (% total) (2015), IDH (2010)
uf.dtypes

# %%
# funçao para converter str para float + alguns replaces de ajustes
def str_to_float(x:str):
    x = float(x.replace(" ", "")
                .replace(",", ".")
                .replace("\xa0", ""))
    return x

# %%
# podemos criar métodos personalizados e aplicar no dataframe utilizando método apply (sem precisar percorrer uma lista de valores com for por exemplo)
# convertendo str para float

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
uf

# %%
uf.dtypes

# %%
# transformar "Expectativa de vida (2016)" em float
def exp_to_anos(exp:str):
    return float(exp.replace(",", ".")
                    .replace("anos", ""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)
uf

# %%
uf.dtypes

# %%
# criando um case when aplicando uma função customizada no dataframe
def uf_to_regiao(uf):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Norte"
    elif uf in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Parana", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"

uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
uf

# %%
def mortalidade_to_float(x:str):
    return float(x.replace("‰", "")
                  .replace(",", ".")
                )

uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)
uf

# %%
# até agora fizemos apply em uma serie, agora faremos uma apply no dataframe
# comparando 3 colunas:
# se PIB per capita for maior que 30.000 + a mortalidade infantil ser maior que 15%00 + o IDH ser maior que 700 -> "Parece bom" ELSE "Não parece bom"

def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (/1000)"] < 15 and
            linha["IDH (2010)"] > 700)
# %%
# aplicando nas linhas

uf.apply(classifica_bom, axis=1)