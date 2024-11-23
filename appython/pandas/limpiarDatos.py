import pandas as pd

#cargar el archivo csv
df = pd.read_csv('data.csv')

#retornar una nueva tabla sin datos nulos
dfn = df.dropna()

#remover las filas con datos nulos con el metodo dropna
df.dropna(inplace = True)

#quitar filas duplicadas
df.drop_duplicates(inplace = True)

#imprimir tabla
print(dfn.to_string())

#cargar el archivo csv
df = pd.read_csv('fechas.csv')

#quitar filas con objetos nulos en fecha
df.dropna(subset=['Fecha'], inplace = True)

#quitar filas con objetos nulos en calorias
df.dropna(subset=['Calorias'], inplace = True)

#quitar filas duplicadas
df.drop_duplicates(inplace = True)

#imprimir tabla entera
print(df.to_string())