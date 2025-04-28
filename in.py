import pandas as pd

# df = pd.read_json('sample_Data.json')

# print('display the info of the dataset')
# print(df.info())

data = {
    'Name': ['John', 'Jane', 'Doe'],
    'Age': [28, 34, 29],
    'City': ['New York', 'Los Angeles', 'Chicago']
    
}

df = pd.DataFrame(data)
print(df.info())
