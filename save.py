import pandas as pd

data = {
    'Name': ['John', 'Jane', 'Doe'],
    'Age': [28, 34, 29],
    'City': ['New York', 'Los Angeles', 'Chicago']
    
}

df = pd.DataFrame(data)
print(df)

# Save the DataFrame to a CSV file
# df.to_csv('output.csv', index=False)

# Save the DataFrame to an Excel file
# df.to_excel('output.xlsx', index=False)

# save the DataFrame to a JSON file
df.to_json('output.json', index=False)

