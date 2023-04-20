# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:22:02 2022

@author: lenovo
"""

#获取鼠标位置
import pyautogui as pg           #没别的作用就单纯换个名字
try:
    ak47=1539
    
    
    win=1543
    
    
    
    pg.moveTo(1767,17,duration=0.1)
    pg.click()

    
    
    pg.moveTo(1757,417,duration=0.1)
    pg.click()
    pg.click()
    
    #pg.moveTo(790,65,duration=0.1)
    #pg.click()
    #pg.typewrite('www.baidu.com')
    
    
    
    
    #pg.press('enter')
    
    
    
    while True:
        x,y=pg.position()        #核心函数pg.position()
        print(str(x)+" "+str(y)) #输出鼠标的x,y
        if x==91 and y==1054:
            pg.click()#右键单击
except KeyboardInterrupt:
    print("\n")


#91 1054








