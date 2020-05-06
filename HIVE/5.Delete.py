import pyhive
import sys
from thrift.Thrift import TType
from pyhive import hive
import pandas as pd

conn=hive.Connection(host='localhost',port=10000,auth='NOSASL', database='CRUD',username='hduser')
cursor=conn.cursor()
Delete=''' DELETE FROM operation where NAME="Karthik"
'''
cursor.execute(Delete)
print("")
