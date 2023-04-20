# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

#作用是求出这一段时间的价值均值（求均值）
def keypoint(line,num,time):    
    ks=0
    a=num-time
    while a<num:
        ks=ks+line[a]        
        a=a+1
    ks=round(ks/(time*1.0),2)
    return ks



def Q(pri,line,bj,bj2,bj3,ying,kui):
    
    
    
    
    a=1
    while a<len(bj):
        
        #对于止盈止损初始化
        ko=0
        #买价
        buy=pri[bj[a-1]]
        #方向
        sign=bj2[a-1]


        #print(pri[bj[a]],line[bj3[a]][1])
        #os.system(-1)
        
        
        b=bj[a-1]
        
        #用x回测移动止盈止损
        x=0
        
        vvv=0
        
        while b<bj[a]:
            if(sign==1):
                jiacha=pri[b]-buy
            else:
                jiacha=buy-pri[b]
           
            
           
            
            #每天交易的时间为下午1点30 到3:00    上午9:00 到11：30 晚上9:00 到11:00
            
            if(x<69):
               if(ko==0):
                  if(jiacha<=-10):
                     #触发成功
                     line[bj3[a]]=line[bj3[a]]+[1]
                     ko=1
            if(ko==0):
                if(jiacha>=80):
                    #触发成功
                    line[bj3[a]]=line[bj3[a]]+[2]
                    ko=2
            
            if(jiacha>12):
                vvv=1
            
            if(x>=69):
                if(ko==0):
                    if(jiacha<=-10):
                        line[bj3[a]]=line[bj3[a]]+[1]
                        ko=1
                    if(vvv==1):
                      if(jiacha<=10):
                        #if(buy<=line[bj3[a]][3]):
                            line[bj3[a]]=line[bj3[a]]+[3]                 
                            line[bj3[a]][5]=50
                            
                            ko=3
                    
                    
                    
                    
            
            
            
            
            
            
            #进行x递增
            x=x+1
            
            b=b+1
        
        #没有触发止盈止损
        if(ko==0):
            line[bj3[a]]=line[bj3[a]]+[0]
        
        
        
        a=a+1
        
    
    
    
    

    
    
    
    
    return line












#打开文件
df = pd.read_excel(r'玻璃回测.xlsx',sheet_name="数据") 
#用于计算每一个具体周期
kv1800=1800
kv60=60
#用于存放全部的时间
time=[]
#用于存放特定的时间位置
time2300=[]
#用于存放价格
pri=[]

#读入数据
a=0
while a<len(df.iloc[:,1]):
    time=time+[float(df.iloc[a,1])]
    pri=pri+[df.iloc[a,2]]
    if(float(df.iloc[a,1])==2300):
        time2300=time2300+[a]
    a=a+1
    

#获取第一个大于长周期的价格，指定时间为第一个23:00出现且大于最大均值
a=0
xd=0
while a<len(time2300)-1:
    if(time2300[a]>kv1800):
        xd=a
        break
    a=a+1


#数据处理后,进行转存
#fix中的分别为  位置,23点价格,1小时均线,30小时均线
fix=[]
while xd<len(time2300):
    fix=fix+[[time2300[xd],pri[time2300[xd]],keypoint(pri,time2300[xd],kv60),keypoint(pri,time2300[xd],kv1800)]]    
    xd=xd+1


#大于则提示开多，小于则提示开空
if(fix[0][2]>fix[0][3]):
    hei=1
else:
    hei=-1

#op所指的数字列为开始列，取第一个分歧点的位置，也就是选取第二个位置开始
a=1
while a<len(fix):
    if(fix[a][2]>fix[a][3]):
       hei2=1
    else:
       hei2=-1
    if(hei2!=hei):
        op=a
        break
    a=a+1

#给数据全部打上标记，现在有提示位的数据都是属于关键数据
a=op
while a<len(fix):
    if(fix[a][2]>fix[a][3]):
        qushi=1
    else:
        qushi=-1
    fix[a]=fix[a]+[qushi]
    a=a+1




#存放初始标记
bj3=[]
bj2=[]
bj=[]
bj3=bj3+[op]
bj2=bj2+[fix[op][4]]
bj=bj+[fix[op][0]]

#对于关键提示点进行标记，多多注意一下
fix[op]=fix[op]+[0]+[0]
#完成全部标记
kx=op
a=op
while a<len(fix):
    if(fix[a][4]!=fix[kx][4]):
        bj=bj+[fix[a][0]]
        bj2=bj2+[fix[a][4]]
        bj3=bj3+[a]
        
        
        fix[a]=fix[a]+[0]
        kx=a
    a=a+1




print(bj,bj2)


#用于回测止盈止损,对fix进行改造
fix=Q(pri,fix,bj,bj2,bj3,52,19)



#模拟买入价格
buy=fix[op][1]
#模拟初始信号
sign=fix[op][4]

#初始利润
lirun=0

#中间利润
lirun2=0

ssss1=[]
ssss2=[]



a=op+1
while a<len(fix):
    
    if(len(fix[a])==7):
        
        ryy=lirun
        
        if(fix[a][4]==1):
            lirun2=buy-fix[a][1]
        else:
            lirun2=fix[a][1]-buy
        
        if(fix[a][6]==1):
            lirun2=-10
        if(fix[a][6]==2):
            lirun2=80
        if(fix[a][6]==3):
            lirun2=fix[a][5]
        
        
        
        
        
        ssss1=ssss1+[lirun2]
        lirun=lirun+lirun2
        
        buy=fix[a][1]
        
        sign=fix[a][4]
        
    a=a+1
    
    
print(fix)
print(ssss1)
print(len(ssss1),lirun)






