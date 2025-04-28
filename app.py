import pandas as pd

# read data from CSV file into a dataframe

df = pd.read_csv("sales_data_sample.csv", encoding="latin1") # utf-8 encoding may not work for all CSV files
# latin1 encoding is used to handle special characters

# read data from excel file into a dataframe
df = pd.read_excel("SampleSuperstore.xlsx" ) # openpyxl is used to read xlsx files

print(df)

# note ---> gcsfs is used to read data from google cloud storage