# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os


#测试输出
def w(w):
    print(w)
    os.system(-1)
#普通长度
def ww(w):
    print(len(w))
    os.system(-1)
#作用是求出这一段时间的价值均值（求均值）
def keypoint(line,num,time):    
    ks=0
    a=num-time
    #b=0
    while a<num:
        ks=ks+line[a]        
        a=a+1
        #b=b+1
    ks=round(ks/(time*1.0),2)
    return ks

#废置
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
        
        #用
        x=0
        
        while b<bj[a]:
            if(sign==1):
                jiacha=pri[b]-buy
            else:
                jiacha=buy-pri[b]
           
            
           
            
           
            
           
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
            
            
            
            
            
            
            
            
            
            b=b+1
        
        #没有触发止盈止损
        if(ko==0):
            line[bj3[a]]=line[bj3[a]]+[0]
        
        
        
        a=a+1
    
    
    
    
    

    
    
    
    
    return line


#找到文件中xlsx后缀的文件，具体看输出
file_names = os.listdir()
a=0
while a<len(file_names):
    aa=str(file_names[a])
    if(aa.find("xlsx")>=0):
        aaa=str(file_names[a])
        break
    a=a+1

#2019-2020
#2020-2021
#2021-2022
#2022-2023

#打开文件
df = pd.read_excel(aaa,sheet_name="数据") 


#用于计算每一个具体周期

''''''
kv1800=360
kv60=12

zhiying=81
zhisun=10                                                                       


#反向触发的止盈
zhiying3=10


#反向触发的止损
zhisun3=10



zhisun2=1
chaoguo=50000

timeo=1500

# 止损2 - 10  超过 - 10  时间 - 23     利润861   时间-1500 873

# 止损2 - 1  超过  - 10  时间 - 23     利润1012  时间-1500 854

# 止损2 - 1  超过  - 11  时间 - 23     利润      时间-1500 840

# 止损2 - 1  超过  - 5  时间 - 23     利润984    时间-1500 712

# 止损2 - 5  超过  - 5  时间 - 23     利润971

# 止损2 - 1  超过  - 1  时间 - 23     利润1008

# 止损2 - 3  超过  - 5  时间 - 23     利润1009   时间-1500  883


#判断是否触发了止盈止损

#用于存放全部的时间





#  1--1077 10
#  10 --976 10


# 10-> [0, 0, 0, 0, 0, 8, -20, -94, 511, 331]   714
# 10    [0, 0, 0, 0, 0, 82, 94, 5, 408, 291]    880                                      880
# 4                                             560

# 7->[18, 180, -41, 7, 155, 107, 189, 38, -28, 122]




time=[]
#用于存放特定的时间位置
time2300=[]
#用于存放价格
pri=[]
#时刻最高价
prig=[]
#时刻最低价
prid=[]
#w(df)
#df中的内容分别是  日期、时间、价格
# years存索引,years2存年份
years=[]
years2=[]
yea=int(df.iloc[0,0][0:4])
years2=years2+[yea]
#读入数据
a=0
while a<len(df.iloc[:,1]):
    #保存时间
    time=time+[float(df.iloc[a,1])]
    #保存价格
    pri=pri+[df.iloc[a,2]]
    prig=prig+[df.iloc[a,3]]
    prid=prid+[df.iloc[a,4]]    
    c=int(df.iloc[a,0][0:4])
    if(c!=yea):
        years=years+[a]
        years2=years2+[c]
        yea=c
    #保存特定的时间的位置
    if(float(df.iloc[a,1])==timeo):
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
# fix -> 234 (时间戳16442、价格、短ma、长ma)
#w(fix)
#w()





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

# op处 2863.33 2868.74
# op前一 2888.08 2856.58
#print(fix[op-1][2],fix[op-1][3])
#w()
# op的位置就是直接开始进行标记的位置




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

print(horeprice)
print(len(horeprice))




horeprice2=[]
a=0
while a<len(horeprice):
    
    #print(len(horeprice[a]))
    
    if(len(horeprice[a])>2):
        horeprice2=horeprice2+[horeprice[a]]
    
    
    
    
    
    
    a=a+1






horeprice=horeprice2
#print(len(horeprice2))


#print(len(horeprice))
#w()


a=0
while a<len(horeprice):
    
    #print(len(horeprice[a]))
    
    
    k=len(horeprice[a])
    b=0
    bb=[]
    while b<k:
        
        #horeprice[a]=horeprice[a]+[horeprice[]
    
        if(b>=1):
            bb=bb+[horeprice[a][b]]
                                   
        
        
        
        b=b+1
    
    horeprice[a]=bb
     

    
    
    
    
    
    a=a+1









#print(horeprice)





#w()

















#判断是否触发了止盈止损
zhiying=80
zhisun=10
a2=0
a=0
a3=0
while a<len(horeprice):
    
    #w(horeprice[a])
    
    att=len(horeprice[a])-1
    
    top1=int(horeprice[a][0][4])
    
    #print(top1)
    #os()
    
    
    
    #prip=[]
    
    
    
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















#  这里弄错了
sss1=0
cy=[]
a=0
while  a<len(horeprice):
    
    a1=len(horeprice[a])-1
    if(horeprice[a][a1]==1):
        cy=cy+[80]
        sss1=sss1+80
    if(horeprice[a][a1]==-1):
        cy=cy+[-10]    
        sss1=sss1-10
    
    top=horeprice[a][0][4]
    k=horeprice[a][a1-1][1]-horeprice[a][0][1]
    k=k*top
    
    
    if(horeprice[a][a1]==0):
        cy=cy+[k]      
        sss1=sss1+k
    
    
    
    
    
    a=a+1










'''


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
        
        
        ssss1=ssss1+[lirun2]
        lirun=lirun+lirun2
        
        buy=fix[a][1]
        
        sign=fix[a][4]
        
    a=a+1
    
    
print(fix)
print(ssss1)
print(len(ssss1),lirun)


#ww(fix)

'''


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




