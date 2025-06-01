# 3. **Filtragem de Dados:**
#    - Filtre os jogos com vendas globais acima da média e conte quantos são.
#    - Filtre os jogos lançados após o ano 2010 e calcule a média das vendas globais desses jogos.

import pandas as pd


df_a = pd.read_csv('vgsales_a.csv')
df_b = pd.read_csv('vgsales_b.csv')


df = pd.concat([df_a, df_b], ignore_index=True)


df.columns = ['Ranking', 'Nome', 'Plataforma', 'Ano_Lancamento', 'Genero',
              'Publicadora', 'Vendas_NA', 'Vendas_EU', 'Vendas_JP', 'Vendas_Outros', 'Vendas_Globais']


df['Vendas_Globais'] = pd.to_numeric(df['Vendas_Globais'], errors='coerce')
df['Ano_Lancamento'] = pd.to_numeric(df['Ano_Lancamento'], errors='coerce')

media_vendas_globais = df['Vendas_Globais'].mean()
jogos_acima_media = df[df['Vendas_Globais'] > media_vendas_globais]
quantidade_acima_media = jogos_acima_media.shape[0]


jogos_apos_2010 = df[df['Ano_Lancamento'] > 2010]
media_vendas_apos_2010 = jogos_apos_2010['Vendas_Globais'].mean()

print(media_vendas_apos_2010)
