#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:05:03 2021

@author: franek
"""

%matplotlib inline
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

boston_dataset = datasets.load_boston()
X_full = boston_dataset.data
Y = boston_dataset.target
print(X_full.shape)
print(Y.shape)

selector = SelectKBest(f_regression,k=1)
selector.fit(X_full,Y)
X = X_full[:,selector.get_support()]
print(X.shape)

def plot_scatter(X,Y, R= None):
    plt.scatter(X,Y, s = 32, marker = "o", facecolors = "black")
    if R is not None:
        plt.scatter(X,R,color = "red", linewidth = 0.5)
    plt.show()
    
plot_scatter(X,Y)

#regressor = LinearRegression(normalize= True).fit(X,Y)
regressor = SVR().fit(X,Y)
plot_scatter(X,Y,regressor.predict(X))