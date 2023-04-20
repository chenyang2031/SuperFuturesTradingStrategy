# -*- coding: utf-8 -*-
import pandas as pd
import math


def keypoint(line,num,time):
    
    ks=0
    a=num-time
    while a<num:
        
        ks=ks+line[a]        
        a=a+1
    ks=round(ks/(time*1.0),2)
    
    return ks
    

def chance20(op,line):
    
    smallsy=0
    test=line[op][4]
    
    
    buy=line[op][1]
    
    cy=[]
    cy2=0
    
    
    a=op
    
    v1=0
    
    v2=0
    
    v3=0
    
    
    
    while a<len(line):
        
        forprice=line[a][1]
        
        if(test==1):
            smallsy=forprice-buy
            if(smallsy>=51):
               if(v3==0):
                v1=1
                v3=1
            if(smallsy<=-49):
              if(v3==0):
                v2=1
                v3=1
                
                
        if(test==-1):
            smallsy=buy-forprice    
            if(smallsy>=51):
               if(v3==0):
                v1=1
                v3=1
            if(smallsy<=-49):
              if(v3==0):
                v2=1
                v3=1

        
        if(test!=line[a][4]):
            #print(line[a][0])
            if(test==1):
             smallsy=line[a][1]-buy
            if(test==-1):
             smallsy=buy-line[a][1]

            if(v1==1):
               smallsy=51
               v1=0
               v3=0
            if(v2==1):
                smallsy=-49
                v2=0
                v3=0


            test=line[a][4]
            buy=line[a][1]
            cy=cy+[smallsy]
            cy2=cy2+smallsy
          
        
        a=a+1
    

    s=0
    
    print("最终利润是这样")
    print(cy,cy2)
    print("截至")
    return s








time=[]
pri=[]

time2300=[]

df = pd.read_excel(r'玻璃回测.xlsx',sheet_name="数据") 

kv1800=1800
kv60=60






#print(df)

a=0
while a<len(df.iloc[:,1]):
    
    #print(df.iloc[a,1],a)
    time=time+[float(df.iloc[a,1])]
    pri=pri+[df.iloc[a,2]]
        

    time2300=time2300+[a]
    
    a=a+1
    print(a)

#print(time2300)

#print(time[time2300[0]],time[time2300[1]],time[time2300[2]])

#获取第一个大于长周期的价格
a=0
xd=0
while a<len(time2300)-1:
    
    if(time2300[a]>kv1800):
        xd=a
        break
        
    a=a+1


#print(time2300[xd])
#v2=keypoint(pri,time2300[xd],kv1800)
#print(v2)

hot=[]
fix=[]
while xd<len(time2300):
    fix=fix+[[time2300[xd],pri[time2300[xd]],keypoint(pri,time2300[xd],kv60),keypoint(pri,time2300[xd],kv1800)]] 
    xd=xd+1
    print(xd)
#print(fix,len(fix))

if(fix[0][2]>fix[0][3]):
    hei=1
else:
    hei=-1

#op所指的数字列为开始列
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
    print(a)

#给数据打上标记
a=op
while a<len(fix):
    if(fix[a][2]>fix[a][3]):
        qushi=1
    else:
        qushi=-1
    fix[a]=fix[a]+[qushi]
    a=a+1
    print(a)





print("分界线")
print("收益为")
print(fix)


www=chance20(op,fix)




kkl=[]



shuju01=0


#op=86

xxx=0

#标志位
ppo=fix[op][4]
#初始金钱
buy=fix[op][1]

a=op


money=0
sum1=0



while a<len(fix):
     
    #if(fix[a][0]==29576):
        #shuju01=a
    
    
    
    if(ppo!=fix[a][4]):
        ryy=money
        
        #获取最大回撤
        #if(ryy>=-1000):
         #   if(ryy<=1000):
        #        if(ryy<xxx):
        #            xxx=ryy
        if(fix[a][4]==1):
            kop=buy-fix[a][1]
        else:
            kop=fix[a][1]-buy
        
        
        
        kkl=kkl+[kop]
        sum1=sum1+kop
        money=money+kop
        
        
        
        buy=fix[a][1]
        
        ppo=fix[a][4]
    
    
    a=a+1
    print(a)








print(kkl)
print(ryy,money)
print("最终")
print(sum1)


#print(xxx)

#print(shuju01)


















