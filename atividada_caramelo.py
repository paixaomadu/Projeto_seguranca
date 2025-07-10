import pandas as pd 
import matplotlib.pyplot as plt

df= pd.read_csv('CARAMELO.csv', sep= ';') # fonte da base de dados

df['Valor de Venda']= df['Valor de Venda'].str.replace(',','.').astype(float) # transformando em float
print(df['Valor de Venda'].dtype)

# Valor de venda por cidades do RJ _________________________________________________________________
df_rj= df.loc[df['Estado Loja']== 'RJ'] # filtrando pra lista ser apenas no estado do rio de janeiro
df_rj= df_rj.groupby('Cidade Loja')['Valor de Venda'].sum().reset_index() 
df_rj= df_rj.sort_values(by= 'Valor de Venda')


# Valor de venda por cidade da loja ________________________________________________________________
df_por_cidade= df.groupby('Cidade Loja')['Valor de Venda'].sum().reset_index()
df_por_cidade= df_por_cidade.sort_values(by= 'Valor de Venda')

# Média de venda por categoria de produto __________________________________________________________
df_por_produto= df.groupby('Categoria Produto')['Valor de Venda'].mean().reset_index()
df_por_produto= df_por_produto.sort_values(by= 'Valor de Venda')

# Valor de venda de marcas que vendem produtos eletronicos __________________________________________
df_eletric= df.loc[df['Categoria Produto']== 'Eletrônicos']
df_eletric= df_eletric.groupby('Marca')['Valor de Venda'].sum().reset_index() 
df_eletric= df_eletric.sort_values(by= 'Valor de Venda')

# Gráfico com o uso da biblioteca ____________________________________________________________________
df_eletric.plot(kind='bar', x= 'Marca', y='Valor de Venda') # kind = tipo, x é eixo x e y é eix y
plt.xlabel('\nMarcas Produto')  # nome do eixo x
plt.ylabel('Valor de Venda') # nome do eixo y
plt.title('Valor de venda por marca') # nome do tiyulo 
plt.show()