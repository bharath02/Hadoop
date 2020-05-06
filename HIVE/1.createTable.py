from pyhive import hive

conn=hive.Connection(host='localhost',port=10000,auth='NOSASL', database='CRUD',username='hduser')
cursor=conn.cursor()
"CREATE TABLE in HIVE Optimized ROW COLUMNAR to perform CRUD operations in HIVE "
CreateTable='''create table operation(ID INT, NAME STRING,ADDRESS STRING, DOB STRING)
               clustered by (ID) into 4 buckets
               stored as orc tblproperties('transaction'='true')'''
cursor.execute(CreateTable)

print("CREATED TABLE")
conn.close()