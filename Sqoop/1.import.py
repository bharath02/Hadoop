import os
dataimport="sqoop import --connect jdbc:mysql://localhost:3306/CpuLogData --username hduser --password hduser --table userinfo --m 1 --target-dir /sqoop/importing"
os.system(dataimport)