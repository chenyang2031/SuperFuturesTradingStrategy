# -*- coding: utf-8 -*-
import pandas as pd

time=[]
pri=[]



df = pd.read_excel(r'玻璃回测2.xlsx',sheet_name="数据") 




print(df)

sk=0
sb=0


a=0
while a<len(df.iloc[:,1])-1:
    
    #print(df.iloc[a,1],a)
    time=time+[float(df.iloc[a,1])]
    pri=pri+[df.iloc[a,2]]
    
    if(float(df.iloc[a,1])-float(df.iloc[a+1,1])>1000):
        sk=sk+1
        
    if(float(df.iloc[a,1])-float(df.iloc[a+1,1])>1000):
        if(float(df.iloc[a,1])!=2300):
            print(float(df.iloc[a,1]),a)
        
    if(float(df.iloc[a,1])==2300):
        sb=sb+1

        
    
    a=a+1
    #print(a)


print(sk,"是否相等于",sb)





























