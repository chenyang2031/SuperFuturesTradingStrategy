# -*- coding: utf-8 -*-
import akshare as ak
import time
import pyautogui as pg           #没别的作用就单纯换个名字
import os



def mean(lst):
    kkk=sum(lst)/len(lst)
    kkk=round(kkk,2)
    return str(kkk)




def fuck():
    
    
    
    
    
    pg.moveTo(1919,1040,duration=0.1)
    pg.click()
    
    
    pg.moveTo(95,1054,duration=0.1)
    pg.click()
    
    time.sleep(5)
    
    pg.moveTo(1048,354,duration=0.1)
    pg.click()    
    pg.typewrite('BestWishes')
    
    pg.moveTo(1308,230,duration=0.1)
    pg.click() 









futures_zh_minute_sina_df = ak.futures_zh_minute_sina(symbol="C2305", period="5")



futures_zh_minute_sina_df222 = ak.futures_zh_minute_sina(symbol="C2305", period="1")

futures_zh_minute_sina_df222=futures_zh_minute_sina_df

close=futures_zh_minute_sina_df['close']

openprize=futures_zh_minute_sina_df['open']


close2=futures_zh_minute_sina_df222['close']

openprize2=futures_zh_minute_sina_df222['open']


closeone=[]

openone=[]

closeold=[]
 
openold=[]

a=0


print(futures_zh_minute_sina_df)


a=81
while a>=69:
    
    closeone=closeone+[float(close2.iloc[len(close)-a-1])]
    
    openone=openone+[float(openprize2.iloc[len(openprize)-a-1])]
    
    a=a-1




a=429
while a>=69:
    
    closeold=closeold+[float(close.iloc[len(close)-a-1])]
    
    openold=openold+[float(openprize.iloc[len(openprize)-a-1])]
    
    
    
    a=a-1









#if(b==1):
#    c="做多"
#if(b==0):
#    c="做空"









print("\n")

print("1小时收盘均线:"+ mean(closeone) +"  ///   30小时收盘均线：  "+mean(closeold))

print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
print(closeone[len(closeone)-1])

print("1小时开盘均线:"+ mean(openone)+"  ///   30小时开盘均线：  "+mean(openold))

print("\n")

print("最后30秒交易 无条件执行,犹豫是你的敌人")
print("未来机会有的是，现在心急，最后必亏钱")
print("   ")

YES=0

a=1528
b=0



if(b==1):
    c="做多"
if(b==0):
    c="做空"
if(a!=0):
   if(b==1):
       print("做多+10  "+">="+str(a+52)+"  "+"<="+str(a-19))
   if(b==0):
       print("做空+10  "+">="+str(a+19)+"  "+"<="+str(a-52))    




print()

print("操作："+c)



if(YES==1):
    fuck()








































































































