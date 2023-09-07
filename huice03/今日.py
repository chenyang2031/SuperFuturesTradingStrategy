# -*- coding: utf-8 -*-
import akshare as ak
import time
import pyautogui as pg           

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





futures_zh_minute_sina_df = ak.futures_zh_minute_sina(symbol="C2311", period="3")
futures_zh_minute_sina_df222 = ak.futures_zh_minute_sina(symbol="C2311", period="3")

#print(futures_zh_minute_sina_df)
#print(len(futures_zh_minute_sina_df))

#import os
#os.system(-1)

futures_zh_minute_sina_df222=futures_zh_minute_sina_df
close=futures_zh_minute_sina_df['close']
openprize=futures_zh_minute_sina_df['open']
close2=futures_zh_minute_sina_df222['close']
openprize2=futures_zh_minute_sina_df222['open']
closeone=[]
openone=[]
closeold=[]
openold=[]



# 1小时收盘均线:2678.42  ///   30小时收盘均线：  2694.25


# 1小时收盘均线:2678.4  ///   30小时收盘均线：  2688.05

# 1小时收盘均线:2675.6  ///   30小时收盘均线：  2693.79



#print(futures_zh_minute_sina_df)


a=0
while a<20:
    closeone=closeone+[float(close2.iloc[len(close)-a-1])]
    openone=openone+[float(openprize2.iloc[len(openprize)-a-1])]
    a=a+1

a=0
while a<600:
    closeold=closeold+[float(close.iloc[len(close)-a-1])]
    openold=openold+[float(openprize.iloc[len(openprize)-a-1])]
    a=a+1


print("\n")
print("1小时收盘均线:"+ mean(closeone) +"  ///   30小时收盘均线：  "+mean(closeold))
print("\n")
print("1小时开盘均线:"+ mean(openone)+"  ///   30小时开盘均线：  "+mean(openold))
print("\n")
print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
print(closeone[0])
print("\n")
print("最后30秒交易 无条件执行,犹豫是你的敌人")
print("未来机会有的是，现在心急，最后必亏钱")
print("   ")
YES=0
a=2843

b=0
if(mean(closeold)<mean(closeone)):
 b=1

if(b==1):
   print("做多  "+">="+str(a+80)+"  "+"<="+str(a-10))
if(b==0):
   print("做空  "+">="+str(a+10)+"  "+"<="+str(a-80))    
print("\n")
if(YES==1):
    fuck()



