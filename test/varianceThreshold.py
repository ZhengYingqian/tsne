# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:09:39 2019

@author: Administrator
"""
#去除超过80%样本是0的特征
from sklearn.feature_selection import VarianceThreshold
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
#print(sel.fit_transform(X))

#单变量特征选择
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
iris = load_iris()

print(iris.data[:5])
X, y = iris.data, iris.target
X.shape
#(150, 4)
X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
#print(X_new)
#(150, 2)

#list 数据改成csv
import pandas as pd
def dataToCsv(file, data, columns, target):
    data = list(data)
    columns = list(columns)
    file_data = pd.DataFrame(data, index=range(len(data)), columns=columns)
    file_target = pd.DataFrame(target, index=range(len(data)), columns=['target'])
    file_all = file_data.join(file_target, how='outer')
    file_all.to_csv(file) 

#dataToCsv('OUT.csv', iris, ['1','2', '3', '4'], '')
import csv
outFile = "test.csv"
 
outFileCsv = open(outFile,"w",newline='')
 #导出字典
fileheader = ['orderid','otime']
outDictWriter = csv.DictWriter(outFileCsv,fileheader)
outDictWriter.writeheader()
# 
##result =[ {'orderid':'abc','otime':44555},{'orderid':'abc','otime':44555}]
#outDictWriter.writerows(X)
#outFileCsv.close()