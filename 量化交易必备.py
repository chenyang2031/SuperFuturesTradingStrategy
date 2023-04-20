# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:17:58 2023

@author: lenovo
"""

from datetime import datetime
from datetime import timedelta
from datetime import timezone
import pyautogui as pg
import time

def Winner():
    
    pg.moveTo(88,1056,duration=0.1)
    pg.click()
    
    
    
    
    pg.moveTo(343,704,duration=0.1)
    pg.click()
    #pg.click()    
    

while(1):

    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    SHA_TZ = timezone(
        timedelta(hours=8),
        name='Asia/Shanghai',
    )
    # 北京时间
    beijing_now = utc_now.astimezone(SHA_TZ)
    #print(beijing_now)
    #print(type(beijing_now))
    fmt = '%Y-%m-%d %H:%M:%S'
    now_fmt =beijing_now.strftime(fmt)
    print(now_fmt)
    
    print(now_fmt[:-2])
    
    print(now_fmt[-2:])
    print(now_fmt[-5:-3])
    print(now_fmt[-8:-6])    
    
    print(type(now_fmt))
    
    
    hour=(int)(now_fmt[-8:-6])
    minute=(int)(now_fmt[-5:-3])    
    second=(int)(now_fmt[-2:])    
    
    
    
    
    
    if(hour==20):
        if(minute==48):
            if(second==30):
                Winner();
                break
    
    
    
    
    
    
    
    #time.sleep(0.2)



print("执行成功，请指示")














