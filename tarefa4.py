#    - Adicione uma coluna ao DataFrame que calcule a soma das vendas na América do Norte e Europa.
#    - Agrupe os dados por ano de lançamento e calcule a média das vendas globais.

import pandas as pd

df_a = pd.read_csv("vgsales_a.csv")
df_b = pd.read_csv("vgsales_b.csv")


df = pd.concat([df_a, df_b], ignore_index=True)


df.rename(columns={'Global_Sales;': 'Global_Sales'}, inplace=True)
df['Global_Sales'] = df['Global_Sales'].astype(str).str.replace(';', '', regex=False).astype(float)


df['NA_EU_Sales'] = df['NA_Sales'] + df['EU_Sales']


media_vendas_por_ano = df.groupby('Year')['Global_Sales'].mean().reset_index()


print("Primeiros registros com a nova coluna 'NA_EU_Sales':")
print(df[['Name', 'NA_Sales', 'EU_Sales', 'NA_EU_Sales']].head())

print("\nMédia das vendas globais por ano de lançamento:")
print(media_vendas_por_ano.head())
