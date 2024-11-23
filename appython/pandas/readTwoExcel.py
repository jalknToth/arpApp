import pandas as pd

# Definir las rutas a los archivos y los nombres de las columnas.
data1 = "datos1.xlsx" 
data2 = "datos2.xlsx"
data1_column = "nombre"
data2_column = "nombre"

def find_duplicate_ids(data1, data1_column, data2, data2_column):

    try:
        # Leer los archivos Excel usando pandas.
        df1 = pd.read_excel(data1)  
        df2 = pd.read_excel(data2) 

    except FileNotFoundError:
        # Capturar el error si uno o ambos archivos no se encuentran.
        return "Uno o ambos archivos no se encontraron."
    except Exception as e:  # Captura errores de lectura más generales.
        # Captura cualquier otro error durante la lectura y devuelve un mensaje descriptivo.
        return f"Error al leer el archivo Excel: {e}"

    if data1_column not in df1.columns:
        return f"Column '{data1_column}' not found in {data1}"
    if data2_column not in df2.columns:
        return f"Column '{data2_column}' not found in {data2}"


    ids1 = set(df1[data1_column])
    ids2 = set(df2[data2_column])
    duplicate_ids = list(ids1.intersection(ids2))
    return duplicate_ids
    """
    try:
        # Convertir las columnas de ID a conjuntos para una comprobación de pertenencia más eficiente.
        ids1 = set(df1[data1_column])  # Crea un conjunto con los IDs del primer archivo.
        ids2 = set(df2[data2_column])  # Crea un conjunto con los IDs del segundo archivo.

    except KeyError:
        # Capturar el error si una o ambas columnas no se encuentran en los archivos.
        return "Una o ambas columnas no se encontraron en los archivos especificados."


    # Encontrar la intersección de los dos conjuntos para obtener los IDs duplicados.
    duplicate_ids = list(ids1.intersection(ids2))  # Encontra los elementos comunes (IDs duplicados).
    return duplicate_ids  # Devolver la lista de IDs duplicados.
    """

# Llama a la función para encontrar los IDs duplicados.
duplicate_ids = find_duplicate_ids(data1, data1_column, data2, data2_column)

# Verifica si el resultado es una lista (lo que significa que no hubo errores).
if isinstance(duplicate_ids, list):  # Comprueba si es una lista o un mensaje de error.
    if len(duplicate_ids) > 0:  # Comprueba si se encontraron duplicados.
        print("IDs duplicados:")
        for id_val in duplicate_ids: # Itera e imprime cada ID duplicado.
            print(id_val)
    else:  # Si no se encontraron duplicados.
        print("No se encontraron IDs duplicados.")
else:  # Si hubo un error (el resultado no es una lista).
    print(duplicate_ids)  # Imprime el mensaje de error.