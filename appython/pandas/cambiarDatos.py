import pandas as pd

#comando para crear ambiente: python -m venv [name]
#comando para activar: source [name]/bin/activate
#comando para instalar libreria: pip install pandas

#cargar el archivo csv
df = pd.read_csv('reportekey.xlsx')

#cambiar la duracion a 120 si es mayor a 120
for x in df.index:
  if df.loc[x, "Usuario"] > 120:
    df.loc[x, "Usuario"] = 120

#elimminar filas si 
for x in df.index: 
  if df.loc[x, "Calorias"] > 400:
    df.drop(x, inplace = True)

#imprimir tabla entera
print(df.head())

#encontrar los duplicados
print(df.duplicated())

#tipo de dato
print(type(df.duplicated()))