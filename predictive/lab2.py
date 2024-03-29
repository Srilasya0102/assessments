# -*- coding: utf-8 -*-
"""lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BFILt0FQBQ8nm_rRP08_VCr5e6jcenAT
"""

import pandas as pd
import pandas as pd
from sklearn import tree
import numpy as np
import warnings as wr
wr.filterwarnings('ignore')
from sklearn.preprocessing import OneHotEncoder
data=pd.read_csv("/content/booking.csv")
df=pd.DataFrame(data)
df.head()
#1
#detecting the null values
df.isnull().sum()
#Identifying  and working the outliers
Q1=df.quantile(0.25)
Q3=df.quantile(0.75)
IQR=Q3-Q1
outliers=((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).sum()
print(outliers)
#2
#encoding the categorical columns
df = pd.DataFrame(data)
print(df)
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(df[['roomtype','type of meal','booking status']])
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(['roomtype','type of meal','booking status']))
print(encoded_data)
print(encoded_df)
#3
df.corr()
#correlations found
df.drop_duplicates()
#duplicate values were dropped
df.nunique()
x=df.iloc[:,:-1]
y=df.iloc[:,-1:]
#4 splitting
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2)
print(y_test)
#5 Training the model
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x_train,y_train)
pred=clf.predict(x_test)
print(pred)
#6 Model Evaluation
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import f1_score
clf_acc = accuracy_score(pred,y_test)
clf_MSE=mean_squared_error(pred,y_test)
clf_RMSE=(clf_MSE).sqrt()
clf_f1score=f1_score(pred,y_test)