import mysql.connector as sql
#import sqlalchemy as sa
import pandas as pd

#cargar el archivo excel
df = pd.read_excel('datos.xlsx')

#agregar una columna con el nombre completo
#df['nombreCompleto'] = df['nombre']+ ' '+ df['apellido']

#imprime los datos de excel
print(df)

#crear la cadena del conector
connector = sql.connect(host="localhost", user="root", password="", database="arpa")

if connector.is_connected():
    print('Well done')
    #perform db operations
else:
    print('Try again')
    
connector.close()

#crear el motor
#engine = sa.create_engine("mysql+pymysql://root:mefort@1ece@localhost/arpa")

#cargar los datos en la base de datos
#df.to_sql(name = 'empleados', con = engine, index = False, if_exists = 'fail')



    
    