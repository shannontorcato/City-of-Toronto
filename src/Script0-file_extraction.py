import os
import requests

# This is the base URL for the PDF files
base_url = 'https://www.trreb.ca/files/market-stats/market-watch/mw{:02d}{:02d}.pdf'

# The start and end years can be modified as needed
start_year = 2022
end_year = 2023

# The start and end months can be modified as needed
start_month = 1
end_month = 2

# The output directory 
output_dir = './data/housing_market_Q1/raw'

# Create a loop for the years and months and save in the output directory
for year in range(start_year, end_year + 1):
    for month in range(start_month, end_month + 1):
        url = base_url.format(year % 100, month)
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(output_dir, os.path.basename(url))
            with open(file_path, 'wb') as file:
                file.write(response.content)
