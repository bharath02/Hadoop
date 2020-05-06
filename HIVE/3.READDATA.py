from pyhive import hive
import pandas as pd

conn=hive.Connection(host='localhost',port=10000,auth='NOSASL', database='CRUD',username='hduser')
cursor=conn.cursor()
read="""SELECT * FROM operation"""
data=pd.read_sql(read,conn)
print(data)