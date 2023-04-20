# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:35:38 2023

@author: lenovo
"""

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

# 读入数据
#data = pd.read_csv('your_data.csv')

time=[]
pri=[]

time2300=[]

df = pd.read_excel(r'玻璃回测.xlsx',sheet_name="数据") 

kv1800=1800
kv60=60

print(df)

a=0
while a<len(df.iloc[:,1]):
    
    #print(df.iloc[a,1],a)
    time=time+[float(df.iloc[a,1])]
    pri=pri+[df.iloc[a,2]]
        
    if(float(df.iloc[a,1])==2300):
        time2300=time2300+[a]

    a=a+1
    #print(a)





data = np.array(pri)

data.reshape(-1,1)



# 数据预处理：标准化
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data)


# 定义网络结构
model = Sequential()
model.add(LSTM(50, input_shape=(1, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# 训练网络
model.fit(data, epochs=100, batch_size=1, verbose=2)


prediction = model.predict(data)



print(prediction)




















