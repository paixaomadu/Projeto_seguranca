import pandas as pd


df= pd.read_csv('2_2024.csv', sep= ';')
df['Valor de Venda']= df['Valor de Venda'].str.replace(',','.').astype(float)
print(df['Valor de Venda'].dtype)

df_etanol= df.loc[(df['Estado - Sigla']== 'RJ') & (df['Produto']== 'ETANOL')]# df.loc -> estrutura de filtro 
df_gasolina= df.loc[(df['Estado - Sigla']== 'RJ') & (df['Produto']== 'GASOLINA')]
df_diesel= df.loc[(df['Estado - Sigla']== 'RJ') & (df['Produto']== 'DIESEL')]

df_media_et= df_etanol.groupby('Bairro')('Produto')['Valor de Venda'].mean().reset_index()
df_media_et= df_media_et.sort_values(by= 'Valor de Venda', ascending= True) #repetir essa estrutura para gasolina e diesel 

df_media_gas= df_gasolina.groupby('Bairro')('Produto')['Valor de Venda'].mean().reset_index() # 
df_media_gas= df_media_gas.sort_values(by= 'Valor de Venda', ascending= True)

df_media_die= df_diesel.groupby('Bairro')('Produto')['Valor de Venda'].mean().reset_index()
df_media_die= df_media_die.sort_values(by= 'Valor de Venda', ascending= True)
#usar o .head -> .para colocar os 5 primeiros numeros e po . tail() para os ultimos

df_media_et.head(5)
df_media_et.tail(5)

df_media_gas.head(5)
df_media_gas.tail(5)

df_media_die.head(5)
df_media_die.tail(5)

df22_1 = pd.read_csv('2022_01', sep= ';')
df22_2 = pd.read_csv('2022_02', sep= ';')
df23_1 = pd.read_csv('2023_01', sep= ';')
df23_2 = pd.read_csv('2023_02', sep= ';')
df24_1 = pd.read_csv('2022_01', sep= ';')
df24_2 = pd.read_csv('2024_02', sep= ';')