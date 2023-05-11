import pandas as pd

# Read the excel file
filepath = 'data/housing_market_Q1/processed/'
input_file_name = 'mw2301-january-city-toronto.xlsx'
df = pd.read_excel('{0}{1}'.format(filepath, input_file_name), sheet_name=None)

df
# Get the sheet names
#sheet_names = df.keys()
#print(sheet_names)