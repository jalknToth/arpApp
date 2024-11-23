import pandas as pd

df = pd.read_excel('byr.xlsx', sheet_name='Sheet1')
cols = df.columns

print(cols)