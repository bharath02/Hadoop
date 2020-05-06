from pyhive import hive
import pandas as pd

conn=hive.Connection(host='localhost',port=10000,auth='NOSASL', database='CRUD',username='hduser')
cursor=conn.cursor()
UPDATEval=''' UPDATE operation set ADDRESS='MNTY'
           where NAME='Karthik'
'''
try:
    cursor.execute(UPDATEval)
    print("Updated Successfully")
except:
    print("NOT updated")
conn.commit()