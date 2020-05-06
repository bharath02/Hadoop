from pyhive import hive

conn=hive.Connection(host='localhost',port=10000,auth='NOSASL', database='CRUD',username='hduser')
cursor=conn.cursor()

insert='''INSERT INTO table operation  values (1,"BHARATH","HYD","02-02-1994"),(2,'Karthik',"GDK","28-05-1996"),(3,"Sandeep","NZB","19-05-1995"),(4,"HUTHASH","NLG","22-09-1994")'''
cursor.execute(insert)