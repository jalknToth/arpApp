import pandas as pd

#cargar el archivo Excel
df = pd.read_excel('data3.xlsx')

#asignar el nombre de la columna
column = 'Pasivos - Valor COP'

# imprime todos los valores de la columna
print("\nLos valores de la columna son:")
print(df[column])

#sumando el total de la columna
total = df[column].sum()
print(f"El total en {column}: {total}")

#imprime el nombre de las columnas
#print(df.columns)

#pd.set_option('display.max_columns', None)    # Show all columns
#print(df) # Print a concise view

# Coloca el maximo numero de filas
#pd.options.display.max_rows = 200

#imprimir todo la tabla
#print(df.iloc[:20, :30])

#imprimir y localizar la fila uno
#print(df.loc[1])

#imprimir la fila uno, y dos
#print(df.loc[[0, 1]])

#calcular el patrimonio por declaracion ano empleado
