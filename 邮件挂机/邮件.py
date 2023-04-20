# -*- coding: utf-8 -*-

import keyring
import datetime
import time
from imbox import Imbox  #导入imbox
import akshare as ak
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mean(lst):
    kkk=sum(lst)/len(lst)
    kkk=round(kkk,2)
    return str(kkk)


def sendMail(mail_content,recv_address):
    # param mail_content 邮件内容
    # param recv_address 接收邮箱
    sender_address = 'chenyang2512cy@foxmail.com'
    sender_pass = 'odqjmupvjnephbde'
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
    ss2="[["+str(closeone[0])+"]]"
    if(b==1):
       ss="[[做多]]"
    if(b==0):
       ss="[[做空]]"   
    print("\n")

    content=ss2+ss+"收盘均线:("+ str(mean(closeone)) +","+str(mean(closeold))+")  "+ "开盘均线:("+ str(mean(openone)) +","+str(mean(openold))+")  "

    sendMail(content,"chenyang2512cy@foxmail.com")

while True:
    with Imbox('smtp.qq.com','chenyang2512cy@foxmail.com','odqjmupvjnephbde') as imbox:
        
        #all_messages = imbox.messages(send_to='chenyang2512cy@foxmail.com')
            all_messages=imbox.messages(unread=True)
            for uid,message in all_messages:
                print('uid',uid)
                print('主题',message.subject)
                
                if(str(message.subject)=="12"):
                    print("YES")
                    
                    text()
                    imbox.mark_seen(uid)
                    imbox.delete(uid)
                else:
                    imbox.mark_seen(uid)
                
                print('文本格式',message.body['plain'])
                print('发件人：',message.sent_from)
                print('收件人：', message.sent_to)
                #print('时间：',message.date)
                print('成功') #读取成功
                imbox.mark_seen(uid)
                time.sleep(10)
    
    

































