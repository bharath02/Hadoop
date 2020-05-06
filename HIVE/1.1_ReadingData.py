from pyhive import hive
import pandas as pd


# Create HIVE Connection
# Student is created Data base in hive
conn= hive.Connection(host="localhost", port=10000,username="hduser", database="student", auth="NOSASL")

# details are table name in hive

data=pd.read_sql("SELECT * FROM details",conn)


print(data)