import pandas as pd

#cargar el archivo csv
df = pd.read_csv('data.csv')

#reemplazar los datos vacios con el metodo fillna
df.fillna('nuevoValor', inplace = True)

#reemplazar los datos vacios en una columna especifica con el metodo fillna
df['nombreColumna'].fillna('nuevoValor', inplace = True)

#reemplazar calculando el valor promedio
media = df['nombreColumna'].mean()
df['nombreColumna'].fillna(media, inplace = True)

#reemplazar calculando el valor que queda en el medio, después de haber ordenado todos los valores de forma ascendente.
mediana = df['nombreColumna'].median()
df['nombreColumna'].fillna(mediana, inplace = True)

#reemplazar buscando el valor que mas se repite
mode = df['nombreColumna'].mode()[0]
df['nombreColumna'].fillna(mode, inplace = True)

