import pandas as pd

data = {
    'fkIdPeriodo': [1, 2, 3],
    'fkIdEstado': [1, 2, 1],  # Example states
    'Año Creación': [2021,2022,2023],
    'Año Envío': [2022,2023,2024],
    'Usuario': ['201', '202', '203'],
    'Nombre': ['Juan Soto', 'Juliana Mesa', 'Joaquin Roa'],
    'Compañía': ['Company A', 'Company B', 'Company A'],
    'Cargo': ['Manager', 'Director', 'Manager'],
    'RUBRO DE DECLARACIÓN': ['Income', 'Assets', 'Income'],
    'fkIdDeclaracion': [101, 102, 103],
    'Patrimonio - Activo': ['Real Estate', 'Stocks', 'Bonds'],
    'Patrimonio - % Propiedad': [100, 50, 25],
    'Patrimonio - Propietario': ['John Doe', 'Jane Doe', 'John Doe'],
    'Patrimonio - Valor Comercial': [1000000, 500000, 250000], 
    'Patrimonio - Comentario': ['Primary Residence', 'Diversified Portfolio', 'Government Bonds'],
    'Patrimonio - % Propiedad_Patrimonio': [100, 50, 25], 
    'Patrimonio - Valor Comercial COP': [4000000000, 2000000000, 1000000000], 
    'Patrimonio - Patrimonio - Valor Corregido': [1000000, 500000, 250000],
    'Patrimonio - ValorCorregido COP': [4000000000, 2000000000, 1000000000], 
    'Pasivos - Entidad Personas': ['Bank A', 'Bank B', None],
    'Pasivos - Tipo Obligación': ['Mortgage', 'Loan', None],
    'fkIdMoneda': [1, 2, None],  
    'Texto Moneda': ['USD', 'EUR', None],
    'Pasivos - Valor': [100000, 50000, None],
    'Pasivos - Comentario': ['Home Mortgage', 'Car Loan', None],
    'Pasivos - Valor COP': [400000000, 200000000, None], # Example COP values
    'Ingresos - fkIdConcepto': [1, 2, 3],  # Example concept IDs
    'Ingresos - Texto Concepto': ['Salary', 'Bonus', 'Interest'],
    'Ingresos - Valor': [50000, 10000, 5000],
    'Ingresos - Comentario': ['Monthly Salary', 'Annual Bonus', 'Bond Interest'],
    'Ingresos - Otros': [None, None, None],
    'Ingresos - Valor_COP': [200000000, 40000000, 20000000], # Example COP values
    'Banco - Entidad': ['Bank C', 'Bank D', 'Bank C'],
    'Banco - Tipo Cuenta': ['Checking', 'Savings', 'Checking'],
    'Banco - Titular': ['John Doe', 'Jane Doe', 'John Doe'],
    'Banco - fkIdPaís': [1, 2, 1], # Example Country IDs
    'Banco - Nombre País': ['USA', 'Canada', 'USA'],
    'Banco - Saldo': [10000, 5000, 20000],
    'Banco - Comentario': ['Main Account', 'Emergency Fund', 'Joint Account'],
    'Banco - Saldo COP': [40000000, 20000000, 80000000], # Example COP values
    'Inversiones - Tipo Inversión': ['Stocks', 'Bonds', 'Real Estate'],
    'Inversiones - Entidad': ['Brokerage A', 'Brokerage B', 'Real Estate Company'],
    'Inversiones - Valor': [100000, 50000, 250000],
    'Inversiones - Comentario': ['Tech Stocks', 'Corporate Bonds', 'Rental Property'],
    'Inversiones - Valor COP': [400000000, 200000000, 1000000000], # Example COP values
}

df = pd.DataFrame(data)

df.to_json('byr.json')

df.to_excel('bienesYRentas.xlsx')