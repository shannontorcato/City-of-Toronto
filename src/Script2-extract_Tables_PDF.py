import tabula
import camelot

pdf_path = "data/housing_market_Q1/preprocessed/mw2303-march-city-toronto.pdf"

df = camelot.read_pdf(pdf_path, pages=1, flavor='stream')

print(df)