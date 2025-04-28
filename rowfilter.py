import pandas as pd 

data = {
    'Name': ['Ram', 'Shyam', 'Mohan', 'Sita', 'Gita', 'leeta'],
    'Age': [28, 34, 29, 22, 25, 30],
    'salary': [50000, 60000, 55000, 45000, 48000, 52000],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'San Diego'],
    'Performance_score': [85, 90, 78, 88, 92, 80],
}

df = pd.DataFrame(data)

high_salary = df[df['salary'] > 50000]
print("Rows with salary greater than 50000:")
print(high_salary)


# Filter rows where salary is greater than 50000 and & less than 60000

filtered_rows = df[(df['salary'] > 50000) & (df['salary'] <= 60000)]
print("Rows with salary greater than 50000 and less than 60000:")
print(filtered_rows)
