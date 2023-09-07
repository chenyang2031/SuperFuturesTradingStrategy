# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:18:36 2019

@author: Admini
"""
import xlrd
import matplotlib.pyplot as plt
def read_20180829():
    fname = "data.xlsx"
    bk = xlrd.open_workbook(fname)
    # shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print("no sheet in %s named Sheet1" % fname)
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    print("nrows %d, ncols %d" % (nrows, ncols))
    # 获取第一行第一列数据
    cell_value = sh.cell_value(1, 0)
    print(cell_value)
    time = []
    single1 = []
    single2 = []
    single3 = []
    # 获取各行数据
    for i in range(1, nrows):
        row_data = sh.cell_value(i, 0)
        # print('time', row_data)
        time.append(row_data)
    for i in range(1, nrows):
        row_data = sh.cell_value(i, 1)
        # print('a', row_data)
        single1.append(row_data)
    for i in range(1, nrows):
        row_data = sh.cell_value(i, 2)
        # print('a', row_data)
        single2.append(row_data)
    for i in range(1, nrows):
        row_data = sh.cell_value(i, 3)
        # print('a', row_data)
        single3.append(row_data)
    return time,single1,single2,single3

time,single1,single2,single3 = read_20180829()
plt.subplot(2, 2, 1)
plt.plot(time, single1)
plt.xlabel("time")
plt.ylabel("single1")
plt.subplot(2, 2, 2)
plt.plot(time, single2)
plt.xlabel("time")
plt.ylabel("single2")
plt.subplot(2, 2, 3)
plt.plot(time, single3)
plt.xlabel("time")
plt.ylabel("single3")
plt.show()


#time时间列     single1   信号值     取前多少个X_data预测下一个数据
def time_slice(time,single,X_lag):
    sample = []
    label = []
    for k in range(len(time) - X_lag - 1):
        t = k + X_lag
        sample.append(single[k:t])
        label.append(single[t + 1])
    return sample,label

sample,label = time_slice(time,single1,5)

from sklearn.externals import joblib
from sklearn.grid_search import GridSearchCV
from sklearn import svm
from sklearn.model_selection import train_test_split

from sklearn.utils import shuffle
import numpy as np



#数据集划分
X_train, X_test, y_train, y_test = train_test_split(sample, label, test_size=0.3, random_state=42)


#数据集掷乱
random_seed = 13
X_train, y_train = shuffle(X_train, y_train, random_state=random_seed)

#参数设置SVR准备
parameters = {'kernel':['rbf'], 'gamma':np.logspace(-5, 0, num=6, base=2.0),'C':np.logspace(-5, 5, num=11, base=2.0)}

#网格搜索：选择十折交叉验证
svr = svm.SVR()
grid_search = GridSearchCV(svr, parameters, cv=10, n_jobs=4, scoring='mean_squared_error')
#SVR模型训练
grid_search.fit(X_train,y_train)
#输出最终的参数
print(grid_search.best_params_)

#模型的精度
print(grid_search.best_score_)

#SVR模型保存
joblib.dump(grid_search,'svr.pkl')

#SVR模型加载
svr=joblib.load('svr.pkl')

#SVR模型测试
y_hat = svr.predict(X_test)

#计算预测值与实际值的残差绝对值
abs_vals= np.abs(y_hat-y_test)

import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
plt.plot(y_test,c='k',label='data')
plt.plot(y_hat,c='g',label='svr model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
plt.subplot(2, 2, 1)
plt.plot(abs_vals)
plt.show()
