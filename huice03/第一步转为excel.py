import pandas as pd
import os



def w():
    os.system(-1)





#设置单元格内表格sheet的名字为详单
writer = pd.ExcelWriter(r'玻璃回测.xlsx')
#设置数据表单
df1 = pd.DataFrame()
df1.to_excel(writer,sheet_name='数据',index=False,header=False,startrow=0, startcol=0)
#格式配置
workbook = writer.book
#选定表格sheet的姓名为详单的sheet
worksheet1 = writer.sheets['数据']
#表格的格式设置
bold = workbook.add_format({
            'bold':  False,  # 字体加粗
            #'border': 1,  # 单元格边框宽度
            'align': 'center',  # 水平对齐方式
            'valign': 'center',  # 垂直对齐方式
            #'fg_color': '#F4B084',  # 单元格背景颜色
            #'text_wrap': True,  # 是否自动换行
            #'font_color': 'red',    加红，可以实现           
})







#找到文件中txt后缀的文件，具体看输出
file_names = os.listdir()
a=0
while a<len(file_names):
    aa=str(file_names[a])
    if(aa.find("txt")>=0):
        aaa=str(file_names[a])
        break
    a=a+1
#print(aaa)








#导入数据并且去掉没有用的三行数据
f = open(aaa,encoding = "utf-8",errors='ignore')
f2=f.readlines()
f2=f2[2:]
f2=f2[:-1]
#print(f2)















#对变量进行初始化操作
w=""
w2=""
w3=""
a=0
a2=0
time=[]
price=[]
time2=[]




#跳过第一个交易日，因为第一个交易日没有意义
while a<len(f2):
    #日期
    w=f2[a][:10]
    #具体时间
    w2=f2[a][11:15]
    if(w2=='2300'):
        a2=a
        break
    #收盘价格
    w3=f2[a][31:35]
    #print(w2)
    a=a+1
a2=a2+1
#print(a2,f2[a2])












#把收盘价、日期、时间保存下来，为之后的计算服务
while a2<len(f2):
    #日期
    w=f2[a2][:10]
    #具体时间
    w2=f2[a2][11:15]
    print(w2)
    #收盘价格
    w3=f2[a2][31:35]
    price=price+[float(w3)]
    time=time+[str(w2)]
    time2=time2+[str(w)]
    a2=a2+1
    
    










#把全部的数据写入excel表格
a=0
while a<len(time2):
 worksheet1.write(a+1,0,time2[a], bold)
 a=a+1
a=0
while a<len(time2):
 worksheet1.write(a+1,1,time[a], bold)
 a=a+1
a=0
while a<len(time2):
 worksheet1.write(a+1,2,price[a], bold)
 a=a+1
#writer.save()
writer.close()


print(price)































