import pandas as pd 

data = {
    'Name': ['Ram', 'Shyam', 'Mohan', 'Sita', 'Gita', 'leeta'],
    'Age': [28, 34, 29, 22, 25, 30],
    'salary': [50000, 60000, 55000, 45000, 48000, 52000],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'San Diego'],
    'Performance_score': [85, 90, 78, 88, 92, 80],
}

df = pd.DataFrame(data)

#display the data frame

print("sample data frame")
print(df)
print("Names (single column returned as a series)")
names = df['Name']
print(names)    

# selecting multiple columns
print("Names and Age (multiple columns returned as a data frame)")
names_and_age = df[['Name', 'Age']]
print(names_and_age)
