# @Date    : 2021-01-15
# @Author  : 小海腾

from sqlalchemy import create_engine
import pandas as pd

user = 'root'
password = '123asd123asd'
address = '127.0.0.1'
port = '3306'
database = 'myshop'

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(user, password, address, port, database))

# args = (1, 25)

sql2 = 'select * from users_userprofile'

# re = engine.execute(sql2).fetchall()
re = pd.read_sql_query(sql2, engine)
print(re)
print(type(re))


# pandas读取数据，返回dataframe
# id = 1
# age = 25
# sql1 = 'select * from users_userprofile where id = {} and age = {}'.format(id, age)
# re = pd.read_sql_query(sql1, engine)
# print(re)
# print(type(re))
# for row, row_plant in re.iterrows():
#     print(row)
#     print(row_plant["name"])


# pandas写入数据表，把dataframe数据写入数据表，参数1、要写入的df；
# 2、要写入的表名；3、数据库链接游标；4、{'fail', 'replace', 'append'},共三项可选；5、是否把df的索引也写成一列
# df = pd.DataFrame({"name": ["王五"], "age": [88], "address": ["成都"], "mobile": ["17521242663"]})
# print(df)
# pd.DataFrame.to_sql(df, name='users_userprofile', con=engine, if_exists='append', index=False)


# pandas删除数据，通过execute执行sql删除语句
# name = '王五'
# sql3 = "delete from users_userprofile where name = '{}'".format(name)
# print(sql3)
# engine.execute(sql3)
# re = pd.read_sql_query(sql2, engine)
# print(re)


# pandas更新update数据，通过execute执行sql更新语句
# 同理可得

