import pandas as pd
import os
df1=pd.DataFrame()
path=os.listdir()
for file in path:
    if file.endswith(".csv") and file!="Combined.csv":
        df=pd.read_csv(file)
        df1=pd.concat([df,df1],ignore_index=True)
a=["Asia Prod 1","Asia Prod 1","Asia Prod 1","Asia Prod 1","Asia Prod 2","Asia Prod 2","Asia Prod 2","Asia Prod 2","Asia Prod 3","Asia Prod 3","Asia Prod 3","Asia Prod 3","NA Prod","NA Prod","NA Prod","NA Prod"]
df1["Eniviornment"]=a
df1[["Eniviornment","Source IP"]].to_csv("Combined.csv",index=False)