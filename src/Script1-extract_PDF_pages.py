import PyPDF2
import os

output_location = 'trial'
output_file_name = 'mw2303.pdf'
input_file_name = 'mw2303-march.pdf'

output_path = os.path.join(os.path.dirname(__file__), 'data/housing_market_Q1/{}'.format(output_location), output_file_name)
# Open the PDF file in read-binary mode
#The location of the input file is relative to the location of the folder in whch the PDF is located
with open('data/housing_market_Q1/raw/{}'.format(input_file_name), 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()
    
    # Specify the pages to extract
    pages_to_extract = [0, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    
    # Loop through the pages and add them to the writer object
    for page_num in pages_to_extract:
        pdf_writer.add_page(pdf_reader.pages[page_num])
    
    # Write the new PDF file
    with open(output_path, 'wb') as new_file:
        pdf_writer.write(new_file)