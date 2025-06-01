# 2. **Análise Exploratória:**
#    - Conte a quantidade de jogos por plataforma.
#    - Calcule a média das vendas globais por plataforma.
#    - Conte a quantidade de jogos por gênero.
import pandas as pd

df_a = pd.read_csv('vgsales_a.csv')
df_b = pd.read_csv('vgsales_b.csv')

df = pd.concat([df_a, df_b], ignore_index=True)


df.columns = ['Ranking', 'Nome', 'Plataforma', 'Ano_Lancamento', 'Genero',
              'Publicadora', 'Vendas_NA', 'Vendas_EU', 'Vendas_JP', 'Vendas_Outros', 'Vendas_Globais']


# primeiras_linhas = df.head()


# info_geral = df.info()
# estatisticas = df.describe(include='all')

# primeiras_linhas, estatisticas

df['Vendas_Globais'] = df['Vendas_Globais'].str.replace(';', '', regex=False)
df['Vendas_Globais'] = pd.to_numeric(df['Vendas_Globais'], errors='coerce')


jogos_por_plataforma = df['Plataforma'].value_counts()
# print(jogos_por_plataforma)

media_vendas_por_plataforma = df.groupby('Plataforma')['Vendas_Globais'].mean()
# print(media_vendas_por_plataforma)

jogos_por_genero = df['Genero'].value_counts()
print(jogos_por_genero)


