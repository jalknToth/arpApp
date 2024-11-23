import pandas as pd 

# un dataframe es un arreglo bidimensional o una tabla con filas y columnas

# crear un dataframe desde dos series 
datos = {
  "calorias": [420, 380, 390],
  "duracion": [50, 40, 45]
}

print(type(datos))

#cargar todos los datos en la tabla
df = pd.DataFrame(datos)

#imprimir la tabla
print(df)

#imprimir y localizar la fila uno
print(df.loc[0])

#imprimir la fila uno, y dos
print(df.loc[[0, 1]])

#nombrar cada fila
dfn = pd.DataFrame(datos, index = ["day1", "day2", "day3"])

#imprimir la tabla
print(dfn)

#localizar la duracion del dia dos
print(dfn.loc["day2"])

def 