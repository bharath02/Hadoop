import pandas as pd
import numpy as np
cpuLog=pd.read_csv("CpuLogData2019-10-24.csv")
filterData=[]
for col in cpuLog.columns:
    col=col.strip()
    col=col.replace(" "," _")
    col=col.replace("/","")
    filterData.append(col)
cpuLog.columns=filterData
indices=[]
for index in cpuLog.index:
    if '2019-10-25' in cpuLog['DateTime'].iloc[index]:
        indices.append(index)
cpuLog.replace(cpuLog.isnull(),0,inplace=True)
cpuLog.fillna(np.nan, inplace=True)
cpuLog.to_csv("userlogFilterData.csv",index=False)