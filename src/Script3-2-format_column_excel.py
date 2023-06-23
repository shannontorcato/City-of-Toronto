import pandas as pd
import re

# Read the excel file
# D:\Jobs\projects\City of Toronto\src\data\housing_market_Q1\processed\mw2303-march-city-toronto.xlsx
filepath = 'data/housing_market_Q1/processed/'
input_file_name = 'mw2301-january-city-toronto.xlsx'
df_original = pd.read_excel('{0}{1}'.format(filepath, input_file_name), sheet_name=None)

df = df_original.copy()

# Get the sheet names
sheet_names = df.keys()
for elements in sheet_names:
    print(elements)

for elements in sheet_names:
    print('df_{}'.format(elements))

df_all_home_type = df.get('all_home_type')
df_detached = df.get('detached')
df_semi_detached = df.get('semi_detached')
df_townhouse = df.get('townhouse')
df_condo_townhouse = df.get('condo_townhouse')
df_condo_apartment = df.get('condo_apartment')
df_link = df.get('link')
df_coop_apartment = df.get('coop_apartment')
df_detached_condo = df.get('detached_condo')
df_co_ownership_apartment = df.get('co_ownership_apartment')
df_index_and_benchmark_price = df.get('index_and_benchmark_price')

df_semi_detached.head()

# Rename the ;Unnamed: 0' column to 'Area'
df_all_home_type.rename(columns={'Unnamed: 0': 'Area'}, inplace=True)
df_detached.rename(columns={'Unnamed: 0': 'Area', 'Abc Abc Active Listings':'Active Listings'}, inplace=True)
df_semi_detached.rename(columns={'Unnamed: 0': 'Area', 'Abc Abc Active Listings':'Active Listings'}, inplace=True)
df_townhouse.rename(columns={'Unnamed: 0': 'Area', 'Abc Abc Active Listings':'Active Listings'}, inplace=True)
df_condo_townhouse.rename(columns={'Unnamed: 0': 'Area', 'Abc Abc Active Listings':'Active Listings'}, inplace=True)
df_condo_apartment.rename(columns={'Unnamed: 0': 'Area', 'Abc Abc Active Listings':'Active Listings'}, inplace=True)
df_link.rename(columns={'Unnamed: 0': 'Area', 'Abc Abc Active Listings':'Active Listings'}, inplace=True)
df_coop_apartment.rename(columns={'Unnamed: 0': 'Area', 'Abc Abc Active Listings':'Active Listings'}, inplace=True)
df_detached_condo.rename(columns={'Unnamed: 0': 'Area', 'Abc Abc Active Listings':'Active Listings'}, inplace=True)
df_co_ownership_apartment.rename(columns={'Unnamed: 0': 'Area', 'Abc Abc Active Listings':'Active Listings'}, inplace=True)

df_semi_detached.head()

#convert this into a dataframe df_all_home_type
data_frames = [df_detached,
               df_semi_detached,
               df_townhouse,
               df_condo_townhouse,
               df_condo_apartment,
               df_link,
               df_coop_apartment,
               df_detached_condo,
               df_co_ownership_apartment
               ]

def extract_number_from_string(column):
    try:
        for i in range(len(column)):
            column[i] = re.findall(r'\d+', column[i])
            column[i] = column[i][0]
    except TypeError:
        pass

for elements in data_frames:
    column = elements['Active Listings']
    extract_number_from_string(column)

for elements in data_frames:
    elements.dropna(inplace=True)

#print data type of 'Dollar Volume' column
for elements in data_frames:
    elements['Dollar Volume'] = elements['Dollar Volume'].replace('[\$,]', '', regex=True).astype(float)
    elements['Average Price'] = elements['Average Price'].replace('[\$,]', '', regex=True).astype(float)
    elements['Median Price'] = elements['Median Price'].replace('[\$,]', '', regex=True).astype(float)

#change column name Dollar Volume to 'Dollar Volume ($)'
for elements in data_frames:
    elements.rename(columns={'Dollar Volume': 'Dollar Volume ($)'}, inplace=True)
    elements.rename(columns={'Average Price': 'Average Price ($)'}, inplace=True)
    elements.rename(columns={'Median Price': 'Median Price ($)'}, inplace=True)

#Do the same process for the all_home_type excel sheet
df_all_home_type.rename(columns={'Dollar Volume': 'Dollar Volume ($)'}, inplace=True)
df_all_home_type.rename(columns={'Average Price': 'Average Price ($)'}, inplace=True)
df_all_home_type.rename(columns={'Median Price': 'Median Price ($)'}, inplace=True)
df_all_home_type['Dollar Volume ($)'] = df_all_home_type['Dollar Volume ($)'].replace('[\$,]', '', regex=True).astype(float)
df_all_home_type['Average Price ($)'] = df_all_home_type['Average Price ($)'].replace('[\$,]', '', regex=True).astype(float)
df_all_home_type['Median Price ($)'] = df_all_home_type['Median Price ($)'].replace('[\$,]', '', regex=True).astype(float)


with pd.ExcelWriter('data/housing_market_Q1/final/{0}'.format(input_file_name)) as writer:
    df_all_home_type.to_excel(writer, sheet_name='all_home_type')
    df_detached.to_excel(writer, sheet_name='detached')
    df_semi_detached.to_excel(writer, sheet_name='semi_detached')
    df_townhouse.to_excel(writer, sheet_name='townhouse')
    df_condo_townhouse.to_excel(writer, sheet_name='condo_townhouse')
    df_condo_apartment.to_excel(writer, sheet_name='condo_apartment')
    df_link.to_excel(writer, sheet_name='link')
    df_coop_apartment.to_excel(writer, sheet_name='coop_apartment')
    df_detached_condo.to_excel(writer, sheet_name='detached_condo')
    df_co_ownership_apartment.to_excel(writer, sheet_name='co_ownership_apartment')
    df_index_and_benchmark_price.to_excel(writer, sheet_name='index_and_benchmark_price')