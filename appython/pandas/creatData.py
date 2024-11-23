import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)

# Helper functions
def generar_id_usuario():
    return str(random.randint(200, 299))

def generar_nombre():
    nombres = ['Juan', 'María', 'Carlos', 'Ana', 'Luis', 'Sofía', 'Diego', 'Valentina', 
              'Andrés', 'Isabella', 'Santiago', 'Camila', 'Gabriel', 'Laura', 'Daniel']
    apellidos = ['Soto', 'Mesa', 'Roa', 'García', 'Rodríguez', 'López', 'Martínez', 
                'Gómez', 'Torres', 'Ruiz', 'Ramírez', 'Flores', 'Vargas', 'Castro']
    return f"{random.choice(nombres)} {random.choice(apellidos)}"

def generar_empresa():
    empresas = ['Empresa A', 'Empresa B', 'Empresa C', 'Firma de Inversión X', 
                'Corporación Global', 'Soluciones Técnicas', 'Finanzas Plus', 'Grupo Consultor']
    return random.choice(empresas)

def generar_cargo():
    cargos = ['Gerente', 'Director', 'Analista Senior', 'Vicepresidente', 
              'Asociado', 'Coordinador', 'Supervisor', 'Líder de Equipo']
    return random.choice(cargos)

# Generate 20 records
n_records = 20
datos = {
    'fkIdPeriodo': list(range(1, n_records + 1)),
    'fkIdEstado': np.random.choice([1, 2, 3], n_records),
    'Año Creación': np.random.choice(range(2020, 2024), n_records),
    'Año Envío': np.random.choice(range(2021, 2025), n_records),
    'Usuario': [generar_id_usuario() for _ in range(n_records)],
    'Nombre': [generar_nombre() for _ in range(n_records)],
    'Compañía': [generar_empresa() for _ in range(n_records)],
    'Cargo': [generar_cargo() for _ in range(n_records)],
    'RUBRO DE DECLARACIÓN': np.random.choice(['Ingresos', 'Activos', 'Pasivos'], n_records),
    'fkIdDeclaracion': list(range(101, 121)),
    'Patrimonio - Activo': np.random.choice(['Bienes Raíces', 'Acciones', 'Bonos', 'Fondos Mutuos', 'Propiedad Comercial'], n_records),
    'Patrimonio - % Propiedad': np.random.choice([25, 50, 75, 100], n_records),
    'Patrimonio - Propietario': [generar_nombre() for _ in range(n_records)],
    'Patrimonio - Valor Comercial': np.random.uniform(100000, 2000000, n_records).round(2),
    'Patrimonio - Comentario': ['Propiedad de Inversión', 'Residencia Principal', 'Casa de Vacaciones', 'Edificio de Oficinas', 'Portafolio de Acciones'] * 4,
    'Patrimonio - % Propiedad_Patrimonio': np.random.choice([25, 50, 75, 100], n_records),
    'Patrimonio - Valor Comercial COP': np.random.uniform(1000000000, 5000000000, n_records).round(0),
    'Patrimonio - Patrimonio - Valor Corregido': np.random.uniform(100000, 2000000, n_records).round(2),
    'Patrimonio - ValorCorregido COP': np.random.uniform(1000000000, 5000000000, n_records).round(0),
    'Pasivos - Entidad Personas': [f"Banco {chr(65 + i % 5)}" for i in range(n_records)],
    'Pasivos - Tipo Obligación': np.random.choice(['Hipoteca', 'Préstamo Vehicular', 'Préstamo Personal', 'Tarjeta de Crédito', 'Préstamo Empresarial'], n_records),
    'fkIdMoneda': np.random.choice([1, 2, 3, 4], n_records),
    'Texto Moneda': np.random.choice(['USD', 'EUR', 'GBP', 'COP'], n_records),
    'Pasivos - Valor': np.random.uniform(10000, 500000, n_records).round(2),
    'Pasivos - Comentario': ['Compra de Vivienda', 'Financiación Vehículo', 'Expansión de Negocio', 'Consolidación de Deuda', 'Préstamo de Inversión'] * 4,
    'Pasivos - Valor COP': np.random.uniform(100000000, 1000000000, n_records).round(0),
    'Ingresos - fkIdConcepto': list(range(1, n_records + 1)),
    'Ingresos - Texto Concepto': np.random.choice(['Salario', 'Bonificación', 'Intereses', 'Dividendos', 'Ingresos por Alquiler'], n_records),
    'Ingresos - Valor': np.random.uniform(5000, 100000, n_records).round(2),
    'Ingresos - Comentario': ['Ingreso Mensual', 'Bono Anual', 'Rendimientos de Inversión', 'Alquiler de Propiedad', 'Honorarios de Consultoría'] * 4,
    'Ingresos - Otros': [None] * n_records,
    'Ingresos - Valor_COP': np.random.uniform(50000000, 500000000, n_records).round(0),
    'Banco - Entidad': [f"Banco {chr(65 + i % 5)}" for i in range(n_records)],
    'Banco - Tipo Cuenta': np.random.choice(['Cuenta Corriente', 'Cuenta de Ahorros', 'Cuenta de Inversión', 'Cuenta de Mercado Monetario'], n_records),
    'Banco - Titular': [generar_nombre() for _ in range(n_records)],
    'Banco - fkIdPaís': np.random.choice(range(1, 6), n_records),
    'Banco - Nombre País': np.random.choice(['Estados Unidos', 'Colombia', 'España', 'México', 'Chile'], n_records),
    'Banco - Saldo': np.random.uniform(1000, 100000, n_records).round(2),
    'Banco - Comentario': ['Cuenta Principal', 'Cuenta de Ahorros', 'Cuenta de Inversión', 'Cuenta Conjunta', 'Cuenta Empresarial'] * 4,
    'Banco - Saldo COP': np.random.uniform(10000000, 400000000, n_records).round(0),
    'Inversiones - Tipo Inversión': np.random.choice(['Acciones', 'Bonos', 'Bienes Raíces', 'Fondos Mutuos', 'ETFs'], n_records),
    'Inversiones - Entidad': [f"Firma de Inversión {chr(65 + i % 5)}" for i in range(n_records)],
    'Inversiones - Valor': np.random.uniform(10000, 500000, n_records).round(2),
    'Inversiones - Comentario': ['Portafolio Diversificado', 'Acciones de Crecimiento', 'Bonos de Renta', 'Fondos Indexados', 'Fideicomiso Inmobiliario'] * 4,
    'Inversiones - Valor COP': np.random.uniform(100000000, 2000000000, n_records).round(0),
}

# Create DataFrame
df = pd.DataFrame(datos)

# Add some data consistency
df['Año Envío'] = df['Año Creación'] + 1  # Ensure send year is after creation year
df.loc[df['Texto Moneda'] == 'COP', 'Pasivos - Valor'] = df.loc[df['Texto Moneda'] == 'COP', 'Pasivos - Valor COP']

# Export to both formats
df.to_json('bienesYRentas_mejorado.json', orient='records', indent=2)
df.to_excel('bienesYRentas_mejorado.xlsx', index=False)

print("Muestra de datos generados:")
print(df[['Nombre', 'Compañía', 'Cargo', 'Patrimonio - Valor Comercial', 'Ingresos - Valor']].head())