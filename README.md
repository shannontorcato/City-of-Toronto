
# City of Toronto Open Source Housing Database and Analysis 

# Objective
This project aims to create an opensource database for the City of Toronto that can be used to to identify areas of the city where the need for affordable housing is greatest, and to provide policymakers with actionable insights and recommendations for addressing the affordable housing crisis in Toronto.

![Data Source Workflow](https://github.com/shannontorcato/City-of-Toronto/blob/master/My%20First%20Board.jpg)

# Methodology
1. **Data Collection**: We will collect data from various sources, including the Toronto Real Estate Board, Statistics Canada, the City of Toronto's Homelessness Dashboard, and other relevant sources. The data will include information on housing prices, rental rates, income levels, household demographics, and homelessness.

2. **Data Preprocessing**: The data will be cleaned, formatted, and preprocessed to ensure that it is ready for analysis. This might include merging data from different sources, geocoding addresses to link the data to specific neighborhoods, and cleaning and formatting the data to ensure that it is consistent and accurate.

3. **Data Analysis**: We will analyze the data using statistical techniques and GIS tools to identify areas of the city where the need for affordable housing is greatest. This might involve identifying neighborhoods with the highest housing costs, rental rates, or concentrations of low-income households. We will also use mapping and visualization tools to help identify spatial patterns and trends in the data.

4. **Reporting and Recommendations**: We will create a report summarizing the findings of our analysis and providing actionable recommendations for policymakers and stakeholders. The report will include maps, charts, and other visualizations to help communicate the data and key insights, as well as specific recommendations for policy interventions that can help address the affordable housing crisis in Toronto.


## Data Collection

First, we started by scraping data from Toronto Region Real Estate (TRREB) website. On the TRREB website we download the PDF files under the Market Watch Archive Section.

### PDF Format
The PDF Document consists of 27 pages of tables for the GTA and also the city of Toronto. Since at the moment we are only focusing on the City of Toronto. So, we have to take the pages containing the tables for the City of Toronto.

In order to extract to extract the relevant pages we use a python script. 

Script1-extract_PDF_pages.py -> In this python code, we mention the relevant pages that needs to be extracted.
