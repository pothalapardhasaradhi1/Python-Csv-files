import os
import pandas as pd
path=os.listdir()
df1=pd.DataFrame()
for file in path:
    if file.endswith(".csv") and file!="Combined.csv":
        df=pd.read_csv(file)
        df1=pd.concat([df,df1],ignore_index=True)
df1["Source IP"].drop_duplicates().to_csv("Combined.csv",index=False)
