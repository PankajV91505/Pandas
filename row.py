# head() -- 5
# tails() -- 5

import pandas as pd
df = pd.read_json('sample_Data.json') 

print('display the first 10 rows of the dataframe')
print(df.head(10))

print('display the last 10 rows of the dataframe')
print(df.tail(10))
