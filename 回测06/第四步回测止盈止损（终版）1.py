# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

def w(w):
    
    print(w)
    os.system(-1)

def ww(w):
    
    print(len(w))
    os.system(-1)

#作用是求出这一段时间的价值均值（求均值）
def keypoint(line,num,time):    
    ks=0
    a=num-time

    while a<num:
        ks=ks+line[a]        
        a=a+1
        
    ks=round(ks/(time*1.0),2)
    return ks


#打开文件
df = pd.read_excel(r'玻璃回测.xlsx',sheet_name="数据") 
#用于计算每一个具体周期
kv1800=360
kv60=12
timec=2300
zhiying=81
zhisun=10





#用于存放全部的时间
time=[]
#用于存放特定的时间位置
time2300=[]
#用于存放价格
pri=[]



#df中的内容分别是  日期、时间、价格

prig=[]
prid=[]


#读入数据
a=0
while a<len(df.iloc[:,1]):
    #保存时间
    time=time+[float(df.iloc[a,1])]
    prig=prig+[df.iloc[a,3]]
    prid=prid+[df.iloc[a,4]]
    pri=pri+[df.iloc[a,2]]
    if(float(df.iloc[a,1])==timec):
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
#print(xd)
#w(time2300)



#经过测试
#  time2300 存放正确 68, 137, 206, 275, 344
#  时间 与 价格 一一对应
#print(time)
#w([1])



#print(len(time2300))
#print(xd)

#数据处理后,进行转存
#fix中的分别为  位置,23点价格,1小时均线,30小时均线
fix=[]

#一共有190天的交易时间
b=0
while xd<len(time2300):
    fix=fix+[[time2300[xd],pri[time2300[xd]],keypoint(pri,time2300[xd],kv60),keypoint(pri,time2300[xd],kv1800)]]    
    b=b+1
    xd=xd+1
#print(b)
#w(b)





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


#剔除去fix中多余的几项,这里是前部切割
a=0
coreprice=[]
while a<len(fix):
    
    if(len(fix[a])>=5):
        coreprice=coreprice+[fix[a]]
    a=a+1
#print(len(coreprice))
#w(coreprice)


#剔除去fix中多余的几项,这里是尾部切割
a=len(coreprice)-1
biao1=coreprice[a][4]
#w(biao1)
a=len(coreprice)-1
while a>=0:
    if(coreprice[a][4]!=biao1):
        break
    a=a-1
coreprice=coreprice[:a+2]

#print(coreprice)

#print(len(coreprice))

top1=coreprice[0][4]
horeprice=[]
koreprice=[]
a=0


#用抽象的方式，单独提取出每一次的交易记录
while a<len(coreprice)-1:
    while(coreprice[a][4]==top1):
     koreprice=koreprice+[coreprice[a]]
     a=a+1
    koreprice=koreprice+[coreprice[a]]
    top1=top1*(-1)
    horeprice=horeprice+[koreprice]
    koreprice=[]
    #a=a+1

#print(horeprice[0][0][1])

#print(len(horeprice))

#w(horeprice[0])


#判断是否触发了止盈止损




#print(horeprice)



#w()





a2=0
a=0
a3=0
while a<len(horeprice):
    
    #w(horeprice[a])
    
    att=len(horeprice[a])-1
    
    top1=int(horeprice[a][0][4])

    first=int(horeprice[a][0][0])
    
    #w(pri)
    
    
    end=int(horeprice[a][att][0])    
    
    a2=first
    
    if(top1>0):
        buy=int(horeprice[a][0][1])
        while a2<end:
          if(buy-int(prid[a2])>=zhisun):
              horeprice[a]=horeprice[a]+[-1]
              a3=1
              break
          if(int(prig[a2])-buy>zhiying):
              horeprice[a]=horeprice[a]+[1]          
              a3=1
              break
          a2=a2+1
    if(top1<0):
        buy=int(horeprice[a][0][1])
        while a2<end:
          #print(a2,len(horeprice[a]))
          if(int(prig[a2])-buy>=zhisun):
              horeprice[a]=horeprice[a]+[-1]
              a3=1
              break
          if(buy-int(prid[a2])>zhiying):
              horeprice[a]=horeprice[a]+[1]          
              a3=1
              break
          a2=a2+1    
          
    #print(a)
    if(a3==0):
      horeprice[a]=horeprice[a]+[0] 
    a3=0
    a2=0
    a=a+1
print(horeprice)



sss1=0
cy=[]
a=0
while  a<len(horeprice):
    
    a1=len(horeprice[a])-1
    if(horeprice[a][a1]==1):
        cy=cy+[zhiying]
        sss1=sss1+zhiying
    if(horeprice[a][a1]==-1):
        cy=cy+[-zhisun]    
        sss1=sss1-zhisun
    
    top=horeprice[a][0][4]
    k=horeprice[a][a1-1][1]-horeprice[a][0][1]
    k=k*top
    
    if(horeprice[a][a1]==0):
        cy=cy+[k]      
        sss1=sss1+k
    
    
    a=a+1

print(cy)
print(sss1)
print(sum(cy))

#cy=ssss1
zuiad=-10
huiche=10
zuiad2=[]
huiche2=[]
a=0
s=0
while a<len(cy):
    s=s+cy[a]
    if(s>zuiad):
        zuiad=s
    if(s<huiche):
        huiche=s
    if(cy[a]>=0):
        zuiad2=zuiad2+[cy[a]]
    if(cy[a]<0):
        huiche2=huiche2+[cy[a]]    
    a=a+1
if(1):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("最大盈利："+str(zuiad)+"  "+"最大亏损："+str(huiche))
    print("平均盈利："+str(round(np.mean(zuiad2),2))+"  "+"平均亏损："+str(round(np.mean(huiche2),2)))    
    print("中位数盈利："+str(np.median(zuiad2))+"  "+"中位数亏损："+str(np.median(huiche2)))
    print("胜率："+str(round(len(zuiad2)/len(cy),2))+"  "+"交易次数："+str(len(cy)))    
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    




