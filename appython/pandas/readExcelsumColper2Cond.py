import pandas as pd

#cargar el archivo Excel
df = pd.read_excel('data3.xlsx')

print(df.columns)

#asignar la columna
column = 'fkIdPeriodo'

# sumando el total de los valores en columna
total = df[column].sum()
print(f"\nEl total en la columna es {column}: {total}")

# Get a list of unique conditions (assuming conditions are in a column named 'Condicion')
conditions = df['Usuario'].unique()

# Calculate and print the sum for each condition
for condition in conditions:
    condition_sum = df.loc[df['Usuario'] == condition, column].sum()
    print(f"El total por el usuario {condition}: {condition_sum}")
    
# Calculate the sum for each condition using groupby
condition_sums = df.groupby('Pasivos - Valor COP')[column].sum()

# Print the results nicely formatted
print("\nTotales por Usuario:")
print(condition_sums)

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

