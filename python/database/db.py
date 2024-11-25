import sql.connector as sql
import waitress as wt
import app
import os

def getDBconnection():
    try:
        arpa = sql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return arpa
    except sql.Error as err:
        print('Error de conexión a la base de datos', err)
        return None
    

if __name__ == '__main__':
    wt.serve(app, host='0.0.0.0', port=8080)