from pandas import read_csv

import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Original DataFrame:")
print(data.head())


one_hot_df = pd.DataFrame()
one_hot_df['robot'] = (data['whoAmI'] == 'robot').astype(int)
one_hot_df['human'] = (data['whoAmI'] == 'human').astype(int)

print("\nOne Hot Encoded DataFrame:")
print(one_hot_df.head())
