# %%
import pandas as pd

s1 = pd.Series([10, 20, 30, 40],
                index=['a', 'b', 'c', 'd'],
                name='minhas_series')

#serie = pd.Series([200, 350, 550], index=['banana', 'prato feito', 'big mac'])
s1 + 10

# %%

medias = [7.5, 8.0, 6.5]
s = pd.Series(medias)

s.mean()

# %%
"""Exercício 1: Diferença entre Rótulo e Posição
Neste exercício, você deve criar uma Series com índices customizados para entender como o loc busca pela "chave" e o iloc busca pela "ordem das linhas"
.
Tarefa:
1) Crie uma Series chamada frutas com os valores: 
2) Defina os índices como: ['maçã', 'banana', 'uva', 'laranja']
3) Desafio:
Use o .loc para retornar a quantidade de 'uva'.
Use o .iloc para retornar o valor que está na segunda posição (índice 1) da sua Series."""

frutas = pd.Series([10, 20, 30, 40], index=['maçã', 'banana', 'uva', 'laranja'])

int(frutas['uva'])

int(frutas.iloc[1])

# %%
"""Exercício 2: O efeito da Ordenação
Este exercício foca em como o índice "anda junto" com o valor, mesmo após alterações na ordem da Series
.
Tarefa:
Crie uma Series com os números 
 e índices numéricos padrão (0 a 3).
Use o método .sort_values() para ordenar a Series de forma crescente
.
Desafio:
Após ordenar, use o .loc para acessar o valor. Qual número retornou? (Dica: o rótulo 0 permanece vinculado ao seu valor original)
.
Use o .iloc para acessar o valor. Qual número retornou agora? (Dica: o iloc olha apenas para a nova primeira posição na memória)
."""

numeros = pd.Series([39, 18, 56], index=[0, 1, 2])
numeros = numeros.sort_values()
numeros.loc[0]
numeros.iloc[0]

# %%
"""Exercício 3: Slicing (Fatiamento) e Acesso Reverso
O iloc é extremamente útil para navegar em fatias dos dados, ignorando completamente os nomes das chaves
.
Tarefa:
Crie uma Series chamada temperaturas com 6 valores quaisquer e use nomes de cidades como índices (ex: 'SP', 'RJ', 'MG', etc.)
.
Desafio:
Use o .iloc para retornar apenas as três primeiras cidades da Series (Slicing [:3])
.
Use o .iloc com índice negativo (-1) para descobrir qual a temperatura da última cidade da sua lista
.
Extra: Tente inverter a ordem da Series usando apenas o .iloc com o comando [::-1]
."""

temperaturas = pd.Series([30, 21, 16, 9, 11, 10], index=['SP', 'RJ', 'MG', 'SC', 'RS', 'PR'])
temperaturas.iloc[:3]
temperaturas.iloc[-1]
temperaturas.iloc[::-1]