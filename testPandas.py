# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

# s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
# d2 = pd.DataFrame(s)
# d.head()
# d.describe()
# data=pd.read_excel("F:\data.xlsx")
# print(data)

# pd.read_csv('F:\data.csv', encoding='utf-8')
# np.random.seed(12345)
# data = pd.DataFrame(np.random.randn(1000, 4))
# print(data[(np.abs(data) > 3).any(1)])  #.any(1) 表示整行都保留

# db = json.load(open('pydata-book/datasets/usda_food/database.json'))
# info_keys = ['description', 'group', 'id', 'manufacturer']
# info = pd.DataFrame(db, columns=info_keys)
# nutrients = []
# for rec in db:2
#     funts = pd.DataFrame(rec['nutrients'])
#     funts['id'] = rec['id']
#     nutrients.append(funts)
# nutrients = pd.concat(nutrients, ignore_index=True)
# nutrients = nutrients.drop_duplicates()


df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})
group = df['data1'].groupby(df['key1'])
for name, groupname in df.groupby('key1'):
    print(name)
    print(groupname)
