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


# Updating values in a DataFrame can be done using the .loc[] method.
# .loc[] 

# df.loc[row_index, "column name"] = new_value

'''
df.loc[0, "salary"] = 60000
print("Data frame after updating salary of Ram:")
print(df)
'''

# Updating multiple values in a DataFrame can be done using the .loc[] method with a list of indices.

# increase_salary by 10% for employees with performance

df["salary"] = df["salary"] * 1.5
print("Data frame after increasing salary by 50%")
print(df)
