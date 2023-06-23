# This script is not being used at the moment.
# Rxtraction of tables from PDF is done usign Excel.
import tabula
import camelot

pdf_path = "data/housing_market_Q1/preprocessed/mw2303-march-city-toronto.pdf"

df = camelot.read_pdf(pdf_path, pages=1, flavor='stream')

print(df)