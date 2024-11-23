import pandas as pd

a = ['Usuario', 'Patrimonio', 'Porcentaje']
c = ['Carlos Mejia',30000000,'50%']

b = pd.Series(a)
print(b)

y = pd.Series(a, index = ['Carlos Mejia',30000000,'50%'])
print(y)
print(type(y))
y.to_excel('y.xlsx')

dictAB = dict(zip(a, c))
print(dictAB)
print(type(dictAB))

df = pd.DataFrame(y)
print(df)