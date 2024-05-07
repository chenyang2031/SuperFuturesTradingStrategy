# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pandas as pd

time=[]
pri=[]



df = pd.read_excel(r'玻璃回测.xlsx',sheet_name="数据") 
sk=0
sb=0
a=0
ktv=[]

while a<len(df.iloc[:,1])-1:
    
    #print(df.iloc[a,1],a)
    time=time+[float(df.iloc[a,1])]
    pri=pri+[df.iloc[a,2]]
    
    if(float(df.iloc[a,1])-float(df.iloc[a+1,1])>1000):
        sk=sk+1
        
    if(float(df.iloc[a,1])-float(df.iloc[a+1,1])>1000):
        if(float(df.iloc[a,1])!=2300):
            print(float(df.iloc[a,1]),a)
            #把数据缺少的位置保存下来
            ktv=ktv+[a]
    if(float(df.iloc[a,1])==2300):
        sb=sb+1

        
    
    a=a+1
    #print(a)


#print(sk,"是否相等于",sb)



di1=[]
di2=[]
di3=[]
di4=[]
di5=[]


a=0
while a<len(df.iloc[:,2]):
    di1=di1+[df.iloc[a,0]]
    di2=di2+[df.iloc[a,1]]    
    di3=di3+[df.iloc[a,2]]   
    di4=di4+[df.iloc[a,3]]      
    di5=di5+[df.iloc[a,4]]      
    
    
    
    a=a+1
    
    
#更正错误
#di2[len(di2)-1]=2300





#print(di2)
#每次把缺少的地方向前推进一位
a=0
b=0
while a<len(ktv):
    print(di2[ktv[a]])
    di2[ktv[a]]=2300
    a=a+1











#写入完整的数据
#设置单元格内表格sheet的名字为详单
writer = pd.ExcelWriter(r'玻璃回测.xlsx')
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
a=0
while a<len(di1):
 worksheet1.write(a+1,0,di1[a], bold)
 a=a+1
a=0
while a<len(di1):
 worksheet1.write(a+1,1,di2[a], bold)
 a=a+1
a=0
while a<len(di1):
 worksheet1.write(a+1,2,di3[a], bold)
 a=a+1
a=0
while a<len(di1):
 worksheet1.write(a+1,3,di4[a], bold)
 a=a+1
a=0
while a<len(di1):
 worksheet1.write(a+1,4,di5[a], bold)
 a=a+1 
 
 
 
 
 
 
writer.save()














