# -*- coding: utf-8 -*-
import pandas as pd

time=[]
pri=[]


#导入数据
df = pd.read_excel(r'玻璃回测.xlsx',sheet_name="数据") 


#数据初始化
sk=0
sb=0
a=0



#检查一下数据是否出现缺少
while a<len(df.iloc[:,1])-1:
    #print(df.iloc[a,1],a)
    time=time+[float(df.iloc[a,1])]
    pri=pri+[df.iloc[a,2]]
    #到达第二天了
    if(float(df.iloc[a,1])-float(df.iloc[a+1,1])>1000):
        sk=sk+1
    if(float(df.iloc[a,1])-float(df.iloc[a+1,1])>1000):
        if(float(df.iloc[a,1])!=2300):
            #出现了具体位置的数据缺少
            print(float(df.iloc[a,1]),a)
    if(float(df.iloc[a,1])==2300):
        sb=sb+1
    a=a+1
#print(a)


#若最后相等，数据则没有缺少
print(sk,"是否相等于",sb)





























