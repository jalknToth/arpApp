import pandas as pd

#cargar el archivo csv
df = pd.read_csv('fechas.csv')

#cambiar el dato de la fila 7
df.loc[7,'Duracion'] = 45

for x in df.index:
  if df.loc[x, "Duracion"] > 120:
    df.loc[x, "Duracion"] = 120

#imprimir tabla entera
print(df.to_string())