import pandas as pd

byr = pd.read_excel('data4.xlsx')

columns = byr.stack()

print(columns)

columns.to_excel('columns.xlsx', index=False )