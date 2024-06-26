# -*- coding: utf-8 -*-
"""lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_F6Hsc9urmCltKKXb0pKJNb4M665tWhO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
data=pd.read_csv('/content/auto-mpg.csv')
df=pd.DataFrame(data)
df.head()
df=pd.DataFrame(data)
df.isnull().sum()
df.fillna(df.mean(),inplace=True)
print(df.isnull().sum())
df.info()
df.describe()
df.duplicated().sum()
df.drop_duplicates()
from scipy.stats import zscore
threshold = 3.0
# z_scores = zscore(df)
# z_scores=zscore(df)
# outliers = np.abs(z_scores) > threshold
# df = df[~outliers]
# plt.figure(figsize=(10, 6))
# sns.boxplot(df)
# plt.show()
# print(df.corr())
# sns.heatmap(df.corr(),cmap="virdis",annot=True)
# plt.show()
x=df.iloc[:,:-1]
y=df.iloc[:,-1:]
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = .2)
clf=LogisticRegression()
clf.fit(x_train,y_train)
pred=clf.predict(x_test)
print(pred)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred,y_test)
print('accuracy=',accuracy)