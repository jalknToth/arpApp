import pandas as pd

# crear diccionario desde dos series
datos = {
  'Motos': ["Suzuki", "Yamaha", "Kawazaki"], 
  'Registros': [3, 7, 2]
}

# convertir en tabla de datos
x = pd.DataFrame(datos)

# imprimir tabla
print(x)

# imprimir tipos de datos
print(type(x))
print(type(pd))
print(type(datos))

# imprimir version de pandas
print(pd.__version__)