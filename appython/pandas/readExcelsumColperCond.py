import pandas as pd

#cargando el archivo Excel
inputFile = 'data3.xlsx'
df = pd.read_excel(inputFile) 

#imprimiendo el numero de columnas y el nombre de las columnas
print('\nEl archivo:', inputFile, 'tiene', len(df.columns), 'columnas')
print('-'*60)
print('Y sus nombres son:\n')
print(df.columns) 
print('-'*60)

#creando las variables
outputFile = 'totalPasivos'
colName = 'Usuario'
userName = 'Nombre'
debt = 'Pasivos - Valor COP'
year = 'Año Creación'

#obteniendo valores unicos
#idUser = df[debt].unique()

#Calculando el total de pasivo por usuario
totalDebtUser = df.groupby(colName)[debt].sum()
# Convert to DataFrame
DFtotalDebtUser = totalDebtUser.to_frame()  
#imprimiendo el total de pasivo por usuario
print("El total de pasivos de", colName,"es de:")
print(DFtotalDebtUser)
print('-'*60)

# Guardar el DataFrame en un archivo Excel
DFtotalDebtUser.to_excel(outputFile) 

print(f"Resultados guardados en {outputFile}")

"""
#Calculando el total de pasivo por usuario per year
totalDebtUserYear = df.groupby([colName, year])[debt].sum()
#imprimiendo el total de pasivo por usuario por año
print("El total de pasivos de", colName, "por", year, "es de:")
print(totalDebtUserYear)
print('-'*60)





#sumar patrimonio propietario
#sumar patrimonnio valor comercial
#Total pasivos
#Total ingresos
#saldo bancos
#total inversiones

#porcentaje de propiedades
#valor comercial patrimonio
#API para conectar el TRM 
#total inversiones (acciones,fondos,cdts)
#bancos (dav,bancol,occid) contar productos por banco.
#Pasivos o Deudas (creditos, hipotecario)

#Total patrimonio+Inversiones+Bancos-Pasivos
#endeudamineto pasivos sobre activos
#Total patrimonnio con porcentaje

#ingresos (arrendamientosPATRIMONIO, honorarios, dividendosACCIONES, interesesCDTS)
#variacion absoluta en el pasivo
#variacion ano actual con ano anterior
"""