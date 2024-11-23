import pandas as pd

try:
    df = pd.read_excel('data.xlsx')  # Asegúrate de que 'Hoja1' sea el nombre correcto de la hoja
except FileNotFoundError:
    print("Error: No se encontró el archivo 'data.xlsx'")
    exit()

# Mostrar las primeras 5 filas
print("Primeras 5 filas:")
print(df.head())

# Mostrar las últimas 5 filas
print("\nÚltimas 5 filas:")
print(df.tail())

# Controlar la visualización
pd.set_option('display.max_columns', 10)   # Mostrar un máximo de 10 columnas
pd.set_option('display.float_format', '{:.2f}'.format)  # Formatear los números flotantes con 2 decimales

# Imprimir el DataFrame (si es necesario)
print(df)