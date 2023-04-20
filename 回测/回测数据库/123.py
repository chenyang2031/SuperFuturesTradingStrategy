# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 00:21:20 2023

@author: lenovo
"""

import akshare as ak
import math

def mean(lst):
    kkk=sum(lst)/len(lst)
    kkk=round(kkk,2)
    return str(kkk)




futures_zh_minute_sina_df = ak.futures_zh_minute_sina(symbol="FG2305", period="5")



futures_zh_minute_sina_df222 = ak.futures_zh_minute_sina(symbol="FG2305", period="1")



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


while a<60:
    
    closeone=closeone+[float(close2.iloc[len(close)-a-1])]
    
    openone=openone+[float(openprize2.iloc[len(openprize)-a-1])]
    
    
    
    a=a+1


a=0
while a<360:
    
    closeold=closeold+[float(close.iloc[len(close)-a-1])]
    
    openold=openold+[float(openprize.iloc[len(openprize)-a-1])]
    
    
    
    a=a+1

print("\n")

print("1小时收盘均线:"+ mean(closeone) +"  ///   30小时收盘均线：  "+mean(closeold))

print("\n")

print("1小时开盘均线:"+ mean(openone)+"  ///   30小时开盘均线：  "+mean(openold))

print("\n")

print("最后30秒交易 无条件执行,犹豫是你的敌人")
print("最重要的策略：只允许在晚上10：50后看盘")


























































































