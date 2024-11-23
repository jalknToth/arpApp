import pandas as pd

#cargar el archivo Excel
df = pd.read_excel('data.xlsx')

#imprime las primeras 5 y ultimas 5 filas
print(df)

# Coloca el maximo numero de filas
pd.options.display.max_rows = 200

#imprimir todo la tabla
print(df.to_string())