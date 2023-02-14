# -*- coding: utf-8 -*-
"""Insurace.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dsj34Te_ZzOPjuss_YiiHwNYAF2RfSzM
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/drive/MyDrive/Smartbridge/insurance.csv')

df.head()

df.head()

df.tail()

df.shape

df.info()

df.columns

df.describe()

df.isnull()

df.isnull().any()

df.isnull().sum()

# df['age'].fillna(df['age'].mean(),inplace=True)

df.head()

df.region.value_counts()

df.sex.value_counts()

df.smoker.value_counts()

"""## **Data Visualizing**"""

sns.distplot(df['age'])

sns.displot(df['age'])

sns.lineplot(df['age'],df['charges'])

plt.pie(df.smoker.value_counts(),colors=['green','red'],labels=['No','yes'],autopct='%1.1f%%')

sns.barplot(df.region.value_counts().index,df.region.value_counts())

sns.scatterplot(x=df.age,y=df.charges)

plt.pie(df.sex.value_counts(),colors=['yellow','blue'],labels=['male','Female'],autopct='%1.1f%%')
plt.title('Gender')

df.hist(figsize=(15,7))

sns.boxplot(df.bmi)

p99=df.bmi.quantile(0.99)
p99

df=df[df.bmi<=p99]
sns.boxplot(df.bmi)

"""# Encoding"""

df.head()

"""Label Encoding"""

from sklearn.preprocessing import LabelEncoder

lb=LabelEncoder()

df.sex=lb.fit_transform(df.sex)
df.smoker=lb.fit_transform(df.smoker)

df.head()

df_onehot=pd.get_dummies(df,columns=['region'])

df_onehot

df_onehot.corr()

plt.figure(figsize=(15,10))
sns.heatmap(df_onehot.corr(),annot=True)

df_onehot.head()

X=df_onehot.drop(columns=['charges'],axis=1)

X.head()

y=df_onehot['charges']

y.head()

from sklearn.preprocessing import scale

x_scale=pd.DataFrame(scale(X),columns=X.columns)

x_scale

