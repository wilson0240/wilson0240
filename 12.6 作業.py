# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:24:49 2019

@author: arthu
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score

AirQ=pd.read_excel('AirQtest.xlsx')

PMs = AirQ[['PM2.5','PM10']].dropna()
X = PMs['PM10']

X = X.as_matrix()
X = np.reshape(X,(-1,1))
Y = PMs['PM2.5']

Y = Y.as_matrix()
Y = np.reshape(Y,(-1,1))

regr = linear_model.LinearRegression()
regr.fit(X,Y)

Y_pred = regr.predict(X)

print('Coefficients: \n',regr.coef_) #跟EXCEL比較斜率
print('Intercept: \n',regr.intercept_)#跟EXCEL比較斜率
print("mean squared error: %.2f" % mean_squared_error(Y,Y_pred)) #平均方根誤差 
print('variance score (R^2): %.2f' % r2_score(Y,Y_pred)) #

plt.scatter(X,Y, color='black')
plt.plot(X,Y_pred,color='blue', linewidth=3)
plt.xlabel('PM10')
plt.ylabel('PM2.5')

import statsmodels.api as sm
model_1 = sm.OLS(Y,X)
results_1 = model_1.fit()
print(results_1.summary())

Y_pred = results_1.predict()
plt.scatter(X,Y, color='black')
plt.plot(X,Y_pred,color='red', linewidth=3)
plt.xlabel('PM10')
plt.ylabel('PM2.5')
#########多變量線性回歸###########
AirQ_NAN = AirQ.dropna()
model_1 = sm.OLS(AirQ_NAN['PM2.5'],AirQ_NAN[['PM10','CO','NOx']])
