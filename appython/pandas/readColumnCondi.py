import pandas as pd

def calculate_conditional_sum(filepath, column_to_sum, conditions):

    try:
        df = pd.read_excel(filepath)  # Read the Excel file into a Pandas DataFrame
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None


    filtered_df = df.copy()  # Create a copy to avoid modifying the original

    for column, value in conditions.items():
        if callable(value):  # Check if the value is a function
            filtered_df = filtered_df[filtered_df[column].apply(value)]
        elif isinstance(value, (list, tuple)): # Check for list or tuple
            filtered_df = filtered_df[filtered_df[column].isin(value)]
        else:
            filtered_df = filtered_df[filtered_df[column] == value]

    if filtered_df.empty:
        return 0  # Return 0 if no rows match the conditions

    return filtered_df[column_to_sum].sum()

filepath = "datos.xlsx"  # Replace with your file path
column_to_sum = "salario" # The column you want to sum

# Example conditions (adapt to your needs):
conditions = {
    "apellido": "Torres"
}

total_sales = calculate_conditional_sum(filepath, column_to_sum, conditions)

if total_sales is not None:
    print(f"Total sales based on conditions: {total_sales}") 
