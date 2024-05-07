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




#2019-2020
#2020-2021
#2021-2022
#2022-2023

#打开文件
df = pd.read_excel(r'玻璃回测.xlsx',sheet_name="数据") 
#用于计算每一个具体周期

''''''
kv1800=1800
kv60=60

zhiying=81
zhisun=10                                                                          

zhisun2=1
chaoguo=50000

timeo=2300

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







#print(horeprice)

#os()




kk2=zhisun

csun=0
oppp=0
oppp2=0
oppp3=0

tyy=0
a2=0
a=0
a3=0
while a<len(horeprice):
    
    #w(horeprice[a])
    
    att=len(horeprice[a])-1
    
    top1=int(horeprice[a][0][4])
    
    first=int(horeprice[a][0][0])
    
    if(top1>0):
        if(len(horeprice[a])>=2):
            if(horeprice[a][1][1]-horeprice[a][0][1]>chaoguo):
                  #first=int(horeprice[a][1][0])
                  #kk2=zhisun2
                  oppp=1
        if(len(horeprice[a])>=3):
            if(horeprice[a][2][1]-horeprice[a][0][1]>chaoguo):
                  #first=int(horeprice[a][1][0])
                  #kk2=zhisun2
                  oppp2=1              
        if(len(horeprice[a])>=4):
            if(horeprice[a][3][1]-horeprice[a][0][1]>chaoguo):
                  #first=int(horeprice[a][1][0])
                  #kk2=zhisun2
                  oppp3=1                    
                  
                  
                  
                  
                  
    if(top1<0):
        if(len(horeprice[a])>=2):
            if(horeprice[a][0][1]-horeprice[a][1][1]>chaoguo):
                  #first=int(horeprice[a][1][0])
                  #kk2=zhisun2
                  oppp=1
        if(len(horeprice[a])>=3):
            if(horeprice[a][0][1]-horeprice[a][2][1]>chaoguo):
                  #first=int(horeprice[a][1][0])
                  #kk2=zhisun2
                  oppp2=1  
                  
        if(len(horeprice[a])>=4):
            if(horeprice[a][0][1]-horeprice[a][3][1]>chaoguo):
                  #first=int(horeprice[a][1][0])
                  #kk2=zhisun2
                  oppp3=1      
    
    
    
    
    
    
    #w(pri)
    
    end=int(horeprice[a][att][0])    
    
    a2=first
    bed=int(horeprice[a][1][0])
    
    if(len(horeprice[a])>=3):
     bed2=int(horeprice[a][2][0])    
    else:
     bed2=999999
    
    if(len(horeprice[a])>=4):
     bed3=int(horeprice[a][3][0])    
    else:
     bed3=999999
    
    
    
    if(top1>0):
        buy=int(horeprice[a][0][1])
        while a2<end:
          
            
          if(a2>bed):
             if(oppp==1):
                  kk2=zhisun2
                  tyy=1
            
          if(a2>bed2):
             if(oppp2==1):
                  kk2=zhisun2
                  tyy=1        
                  oppp=1
            
          if(a2>bed3):
             if(oppp3==1):
                  kk2=zhisun2
                  tyy=1   
                  oppp=1
            
            
          if(buy-int(prid[a2])>=kk2):
              
              if(oppp==0):
               horeprice[a]=horeprice[a]+[-1]
              if(oppp==1):
                 if(tyy==1):
                   horeprice[a]=horeprice[a]+[-2] 
                 else:
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
            
            
          if(a2>bed):
             if(oppp==1):
                  kk2=zhisun2
                  tyy=1
            
          if(a2>bed2):
             if(oppp2==1):
                  kk2=zhisun2
                  tyy=1        
                  oppp=1
            
          if(a2>bed3):
             if(oppp3==1):
                  kk2=zhisun2
                  tyy=1   
                  oppp=1 
            
          #print(a2,len(horeprice[a]))
          if(int(prig[a2])-buy>=kk2):
              
              if(oppp==0):
               horeprice[a]=horeprice[a]+[-1]
              if(oppp==1):
                 if(tyy==1):
                   horeprice[a]=horeprice[a]+[-2] 
                 else:
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
    oppp=0
    oppp2=0
    oppp3=0
    tyy=0
    a=a+1
    kk2=zhisun
    
    
    
#print(horeprice)






a1=len(horeprice[0])-1
#print(horeprice[0][a1-1][0])


a2=horeprice[0][0][0]



#[200,400] 500

yyee=len(years)

vyear=[]
vvyear=[]

#  这里弄错了
sss1=0
cy=[]
a=0
cgg=0

while  cgg<yyee:
    
    #进行多少次迭代意味着多少个年份
    
    while cgg<yyee:
    
        
        #进行退出的条件
        a3=horeprice[a][0][0]
        if(a3>=years[cgg]):
            cgg=cgg+1
            break
        
        
        a1=len(horeprice[a])-1
        if(horeprice[a][a1]==1):
            cy=cy+[zhiying]
            vyear=vyear+[zhiying]
            sss1=sss1+zhiying
        if(horeprice[a][a1]==-1):
            cy=cy+[-zhisun]    
            vyear=vyear+[-zhisun]
            sss1=sss1-zhisun
            
        if(horeprice[a][a1]==-2):
            cy=cy+[-zhisun2]    
            vyear=vyear+[-zhisun2]
            sss1=sss1-zhisun2           
            
            
            
        
        top=horeprice[a][0][4]
        k=horeprice[a][a1-1][1]-horeprice[a][0][1]
        
        if(top>0):
            top=1
        if(top<0):
            top=-1        
        
        
        k=k*top
        
        
        if(horeprice[a][a1]==0):
            cy=cy+[k]   
            vyear=vyear+[k]
            sss1=sss1+k
        
        
        
        
        horeprice[a][a1-1][0]
        
        a=a+1
        
    
    
    
    vvyear=vvyear+[vyear]
    vyear=[]

    

srt=[]
while  a<len(horeprice):
    
    a1=len(horeprice[a])-1
    if(horeprice[a][a1]==1):
        srt=srt+[zhiying]
        cy=cy+[zhiying]
        sss1=sss1+zhiying
        
    if(horeprice[a][a1]==-1):
        srt=srt+[-zhisun]    
        cy=cy+[-zhisun]
        sss1=sss1-zhisun
    

    if(horeprice[a][a1]==-2):
        srt=srt+[-zhisun2]    
        cy=cy+[-zhisun2]
        sss1=sss1-zhisun2


    
    top=horeprice[a][0][4]
    
    
    
    k=horeprice[a][a1-1][1]-horeprice[a][0][1]
    
    
    if(top>0):
        top=1
    if(top<0):
        top=-1
    
    k=k*top
    
    
    if(horeprice[a][a1]==0):
        srt=srt+[k]      
        cy=cy+[k]        
        sss1=sss1+k        
        

    a=a+1



vvyear=vvyear+[srt]










chaE=[]

print(horeprice)

print(len(horeprice))

b=0
a=0
while a<len(horeprice):
    
    b=abs( horeprice[a][0][2] - horeprice[a][0][3] )
    b=round(b,2)
    chaE=chaE+[b]
    a=a+1




#print(chaE)
#print(len(chaE))





#os(-1)
















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


summ=0
year3=[]

a=0
b=0
while a<len(vvyear):
    
    while b<len(vvyear[a]):
        
        summ=summ+vvyear[a][b]
        #if(summ>=212):
        #    break
        
        
        
        b=b+1
    
    
    year3=year3+[summ]
    summ=0
    b=0
    a=a+1


print(year3)


print("所有年份的总收入：")
print(sum(year3))




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







print()
print("进行额度处理后：")

#<131>
# 5----147
# 6----178
# 7----177

#<161>
# 5----234
# 6----221
# 7----214


#<53>
# 5----96
# 6----95
# 7----115

#<166>
# 5----225
# 6----245
# 7----255


#<980>
# 
# 6----901


# <97 57>
# <40 73>




a=0
kvv=[]
while a<len(cy):
    if(chaE[a]>=6):
      kvv=kvv+[cy[a]]
    a=a+1
      
      

cy=kvv    
    
    
summ=0
year3=[]

a=0
b=0

print(cy)

print("所有年份的总收入：")




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
    
    



print(chaE)






























