from pyhive import hive
import pandas as pd


# Create HIVE Connection
# Student is created Data base in hive
conn= hive.Connection(host="localhost", port=10000,username="hduser", database="CRUD", auth="NOSASL")
cursor=conn.cursor()
# Merging operation
mergeOPeration="""MERGE INTO MergeOne SCR ON SCR.id = TRG.id WHEN  NOT MATCHED THEN INSERT VALUES (SCR.id,SCR.FirstName,SCR.LastName)"""

cursor.execute(mergeOPeration)
data=pd.read_sql(mergeOPeration,conn)
print(data)
