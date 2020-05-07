from pyhive import hive
import pandas as pd


# Create HIVE Connection
# Student is created Data base in hive
conn= hive.Connection(host="localhost", port=10000,username="hduser", database="CRUD", auth="NOSASL")
cursor=conn.cursor()
# join operation
joinOPeration="""Select address, firstTable.name, firstTable.age from secondTable JOIN firstTable ON(secondTable.id=firstTable.id)"""
cursor.execute(joinOPeration)
data=pd.read_sql(joinOPeration,conn)
print(data)
