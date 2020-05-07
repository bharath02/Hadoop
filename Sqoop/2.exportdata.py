import os
dataexport="sqoop export --connect jdbc:mysql://localhost:3306/CpuLogData --username hduser --password hduser --table exportUserinfo --export-dir /sqoop/importing/part-m-00000 --m 1"
os.system(dataexport)
