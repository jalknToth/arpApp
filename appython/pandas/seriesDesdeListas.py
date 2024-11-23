import pandas as pd 

#serie es como una columna en una tabla

#crear la lista
a = [1, 2, 3]

#convertir la lista en serie
x = pd.Series(a)

#convertir en serie y nombrar cada fila
y = pd.Series(a, index = ['x','y','z'])

#imprimir serie
print(y)

#imprimir la primer fila
print(x[0])

#accesar al nombre de la fila
print(y['y'])