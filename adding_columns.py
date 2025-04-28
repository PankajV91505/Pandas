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

df["Bonus"] = df["salary"] * 0.1
print("Data frame after adding Bonus column:")
print(df)

# using insert() to add a column at a specific position
# df.insert(loc,"column_name", same_data)

df.insert(0, "Employee_ID", [101, 102, 103, 104, 105, 106])
print("Data frame after inserting Employee_ID column at position 0:")
print(df)