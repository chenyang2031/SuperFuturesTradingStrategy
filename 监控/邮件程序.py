#coding=utf-8
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import akshare as ak
import time
import pyautogui as pg  
from datetime import datetime
from datetime import timedelta
from datetime import timezone
import pyautogui as pg
import time

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



def text():
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
    
    
    #print(futures_zh_minute_sina_df)
    
    
    a=0
    while a<12:
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
    

    content="收盘均线:("+ str(mean(closeone)) +","+str(mean(closeold))+")  "+ "开盘均线:("+ str(mean(openone)) +","+str(mean(openold))+")  "

    sendMail(xc,"chenya2cy@fil.com")
    
    
    
    return content
    
    






def sendMail(mail_content,recv_address):
    # param mail_content 邮件内容
    # param recv_address 接收邮箱
    sender_address = 'chenyang2y@foxl.com'
    sender_pass = ''
    # 怎么申请应用密码可以往下看
    message = MIMEMultipart() #message结构体初始化
    message['From'] = sender_address #你自己的邮箱
    message['To'] = recv_address #要发送邮件的邮箱
    message['Subject'] = mail_content
    # mail_content,发送内容,这个内容可以自定义,'plain'表示文本格式
    message.attach(MIMEText(mail_content,'plain'))
    # 这里是smtp网站的连接,可以通过谷歌邮箱查看,步骤请看下边
    session = smtplib.SMTP('smtp.qq.com', 25)
    # 连接tls
    session.starttls()
    # 登陆邮箱
    session.login(sender_address,sender_pass)
    # message结构体内容传递给text,变量名可以自定义
    text = message.as_string()
    # 主要功能,发送邮件
    session.sendmail(sender_address,recv_address,text)
    # 打印显示发送成功
    print("send {} successfully".format(recv_address))
    # 关闭连接
    session.quit()






main_content = '今天可以进行操作,触发成功'
'''代码就是这么多
是不是很简单。
ok了家人们,记得点一个赞。
'''





while True:
    
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
        
        
        
        
        
        if(hour==5):
            if(minute>=45):
                    xc=text()
                    sendMail(xc,"chen25cy@fmal.com")
                    
        
        if(hour==6):
            break
        
        
        
        
        
        time.sleep(120)
    
    
    
    
    
    








#sendMail(main_content,"chenyancy@foxil.com")









































