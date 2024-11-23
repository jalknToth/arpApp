import pandas as pd
import matplotlib.pyplot as plt

#comando para crear ambiente: python -m venv [name]
#comando para activar: source [name]/bin/activate
#comando para instalar librerias: pip install pandas matplotlib pyplot
#python -m pip install mysql-connector-python
#pip install mysql.connector

#csv es un archivo separado con coma ej. dia,mes,hora/01,03,1340

#cargar el archivo csv
df = pd.read_csv('data.csv')

#imprime las primeras 5 filas
print(df.head())

#imprime las primeras 10 filas
print(df.head(10))

#imprime las ultimas cinco filas
print(df.tail())

#obtener informacion del grupo de datos
print(df.info())

#muestra la relacion entre filas
print(df.corr())

#visualiza el diagrama en un png
df.plot()
# En lugar de plt.show(), usar plt.savefig()
plt.savefig('analisisDatos.png')

#crear un diagrama de dispercion
df.plot(kind = 'scatter', x = 'Duracion', y = 'Calorias')
# En lugar de plt.show(), usar plt.savefig()
plt.savefig('analisisDatoScatter.png')

#crear un histograma pulsacion
df["Pulsacion"].plot(kind = 'hist')
# En lugar de plt.show(), usar plt.savefig()
plt.savefig('analisisDatosHist.png')

