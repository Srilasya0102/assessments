# -*- coding: utf-8 -*-
"""lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UUE7qckHLTZxZNvRu7izoQrV5gnJQnqN
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
data=pd.read_csv('/content/loan_approval.csv')
df=pd.DataFrame(data)
df.columns = df.columns.str.strip()
data.columns = data.columns.str.strip()
df.head()
df.isnull().sum()
df.fillna(df.mean(),inplace=True)
print(df.isnull().sum())
df.info()
df.describe()
df.duplicated().sum()
df.drop_duplicates()
# threshold = 3.0
# z_scores=zscore(df)
# outliers = np.abs(z_scores) > threshold
# df = df[~outliers]
# plt.figure(figsize=(10, 6))
# sns.boxplot(df)
# plt.show()
# print(df.corr())
# sns.pairplot(df)
# plt.show()
la=[]
for i in df['income_annum']:
  if i in range(2500000):
    la.append('Effective')
  elif i in range(2500000,5000000):
    la.append('Efficient')
  else:
    la.append('Fair')
data['Approval']=la
encoder = OneHotEncoder(sparse_output=False)
one_hot_encoded = encoder.fit_transform(df[["education","self_employed","loan_status"]])
one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(["education","self_employed","loan_status"]))
df_encoded = pd.concat([df, one_hot_df], axis=1)
df_encoded = df_encoded.drop(["education","self_employed","loan_status"], axis=1)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data['Approval']=le.fit_transform(data['Approval'])
y=df_encoded.iloc[:,3:4]
x=df_encoded.drop(['Approval'],axis=1)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = .2)
print(df_encoded)
clf=RandomForestClassifier()
clf.fit(x_train,y_train)
pred=clf.predict(x_test)
print(pred)
for i in pred:
  if  i<2500000:
    print('Effective')
  elif i in range(2500000,5000000):
    print('Efficient')
  else:
    print('Fair')
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred,y_test)
print('accuracy=',accuracy)

df

