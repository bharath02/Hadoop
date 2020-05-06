from pyhive import hive
import pandas as pd


# Create HIVE Connection
conn= hive.Connection(host="localhost", port=10000,username="hduser", database="student", auth="NOSASL")

#data=pd.read_sql("SELECT * FROM details",conn)
print(conn)