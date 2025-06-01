# 1. **Leitura e Inspeção dos Dados:**
#    - Carregue os arquivos CSV em DataFrames separados.
#    - Combine os DataFrames em um único DataFrame.
#    - Renomeie as colunas para português
#    - Exiba as primeiras 5 linhas do DataFrame combinado.
#    - Exiba informações gerais e estatísticas descritivas do DataFrame.

import pandas as pd


df_a = pd.read_csv('vgsales_a.csv')
df_b = pd.read_csv('vgsales_b.csv')


df = pd.concat([df_a, df_b], ignore_index=True)


df.columns = ['Ranking', 'Nome', 'Plataforma', 'Ano_Lancamento', 'Genero',
              'Publicadora', 'Vendas_NA', 'Vendas_EU', 'Vendas_JP', 'Vendas_Outros', 'Vendas_Globais']


primeiras_linhas = df.head()


info_geral = df.info()
estatisticas = df.describe(include='all')

primeiras_linhas, estatisticas


