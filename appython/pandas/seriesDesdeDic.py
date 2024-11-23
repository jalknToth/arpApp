import pandas as pd

#una serie es como una columna en una tabla

# crear diccionario
kilometros = {"dia1": 50, "dia2": 60, "dia3": 70}

# convertir diccionario en serie
x = pd.Series(kilometros)

# obtener dia 1
dia1 = pd.Series(kilometros, index = ['dia1'])

# imprimir todos los dias
print(x)

# imprimir dia 1
print(dia1)