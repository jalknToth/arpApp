import pandas as pd

#csv es un archivo separado con coma ej. dia,mes,hora/01,03,13:40

#cargar el archivo csv
df = pd.read_csv('data.csv')

#imprime las primeras 5 y ultimas 5 filas
print(df)

# Coloca el maximo numero de filas
pd.options.display.max_rows = 200

#imprimir todo la tabla
print(df.to_string())