import pandas as pd 

data = {
    'Name': ['Ram', 'Shyam', 'Mohan', 'Sita', 'Gita', 'leeta'],
    'Age': [28, 34, 29, 22, 25, 30],
    'salary': [50000, 60000, 55000, 45000, 48000, 52000],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'San Diego'],
    'Performance_score': [85, 90, 78, 88, 92, 80],
}

df = pd.DataFrame(data)
print(df)

# df.drop(columns=['column_name'], inplace=True) # to remove a column from the data frame
# df.drop(index=[row_index], inplace=True) # to remove a row from the data frame    

print("modified data")
df.drop(columns=['City'], inplace=True) # to remove a column from the data frame
print(df)