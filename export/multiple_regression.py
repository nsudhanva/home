
# coding: utf-8

# # Applying Machine Learning and Deep Learning to identify home appliances consuming excess power
# 
# ## Copyright (c) 2018, Faststream Technologies
# ## Author: Sudhanva Narayana

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib


# ### Import dataset ignoring headers

# In[2]:


df = pd.read_csv('../data/trial_1/home_data.csv')


# ### Dataset

# In[3]:


df.head()


# ### Importing dataset

# In[4]:


X = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8]].values
y = df.iloc[:, 9].values


# ### Encoding Categorical Variables

# In[5]:


# Encoding categorical data
labelencoder_X_0 = LabelEncoder()
X[:, 0] = labelencoder_X_0.fit_transform(X[:, 0])
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
labelencoder_X_3 = LabelEncoder()
X[:, 3] = labelencoder_X_3.fit_transform(X[:, 3])
labelencoder_X_4 = LabelEncoder()
X[:, 4] = labelencoder_X_4.fit_transform(X[:, 4])
labelencoder_X_5 = LabelEncoder()
X[:, 5] = labelencoder_X_5.fit_transform(X[:, 5])
labelencoder_X_6 = LabelEncoder()
X[:, 6] = labelencoder_X_6.fit_transform(X[:, 6])

onehotencoder = OneHotEncoder(categorical_features=[0, 1, 2, 3, 4, 5, 6])
hot_X = onehotencoder.fit_transform(X).toarray()


# ### Avoiding the dummy variable trap

# In[6]:


columns = df.columns
dummies = []
dummies_sum = 0
categories = [0, 1, 2, 3, 4, 5, 6]

for category in categories:
    dummies_sum += category * (df.iloc[:, category].unique().size)
    dummies.append(dummies_sum)
    
# Removing dummy variables
hot_X = np.delete(hot_X, dummies, 1)


# ### Splitting the dataset into the Training set and Test set (75%, 25%)

# In[7]:


X_train, X_test, y_train, y_test = train_test_split(hot_X, y, test_size=0.25, random_state=0)


# ### Multiple Linear Regression

# In[8]:


regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[9]:


y_pred = regressor.predict(X_test)
y_pred


# In[10]:


joblib.dump(regressor, '../model/multiple_reg.pkl') 


# In[11]:


print("Mean Absolute Error: ", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error: ", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: ", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

