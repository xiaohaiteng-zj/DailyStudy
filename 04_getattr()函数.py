# @Date    : 2021-01-15
# @Author  : 小海腾

import pandas as pd
import numpy as np


# getattr()函数用于返回一个对象属性值。
# getattr(object, name[, default])
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})
print(df)
tmp_list = []
for row in df.itertuples():
    # row是一个对象Pandas(Index=0, a=1, b='a')
    print(row)
    tmp_list.append({getattr(row, 'b'): getattr(row, 'a')})
    re = getattr(row, 'b')
    print(re)
print(tmp_list)

dic = {"wh": "bj"}

li = [
    {"bj": "wh"},
    {"bj": "cd"},
    {"tc": "wh"},
    {"tc": "gz"},
]

if {"bj": "wh"} in li:
    print("hahahahh")

if {dic["wh"]: 'wh'} in li:
    print("11111111111111111111")
