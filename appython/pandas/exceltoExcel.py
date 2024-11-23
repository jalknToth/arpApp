import pandas as pd

# Loading the Excel file
inputFile = 'data3.xlsx'
df = pd.read_excel(inputFile)

print(df)

# Specifying the output Excel file
outputFile = 'byr.xlsx'  

# Saving the DataFrame to the new Excel file
df.to_excel(outputFile, index=False) 

print("DataFrame saved to ", outputFile) 
