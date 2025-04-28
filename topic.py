"""
1 - how is big is your data frame
2 - how many columns and rows are there in your data frame

shape() -- (rows, columns)
columns() -- (columns,)
"""

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

print(f'shape of the data frame: {df.shape}')
print(f'columns of the data frame: {df.columns}')