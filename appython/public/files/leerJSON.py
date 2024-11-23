import pandas as pd

#Json es un texto plano con formato de un objeto, muuy conocido en programacion

#cargar el archivo json
df = pd.read_json('data.json')

#imprime las primeras 5 y ultimas 5 filas
print(df)

#imprime todo la tabla
print(df.to_string())

#imprimir que tipo de dato es
print(type(df))
print(type(pd))