import pandas as pd

inputFile = './inputFiles/data3.xlsx'
outputFile = './outputFiles/byr.xlsx' 

# Loading the Excel file
df = pd.read_excel(inputFile)

# Saving the DataFrame to the new Excel file
df.to_excel(outputFile, index=False) 

print("DataFrame saved to ", outputFile)