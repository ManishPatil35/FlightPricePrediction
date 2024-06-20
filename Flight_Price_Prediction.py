#!/usr/bin/env python
# coding: utf-8

# In[179]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[180]:


df_train = pd.read_excel(r'C:\Users\MANISH\Desktop\Flight_Price_Prediction\Data_Train.xlsx')


# In[181]:


df_train.head()


# In[182]:


df_train.shape


# In[183]:


df_test = pd.read_excel(r'C:\Users\MANISH\Desktop\Flight_Price_Prediction\Test_set.xlsx')


# In[184]:


df_test.head()


# In[185]:


df_test.shape


# In[186]:


df = pd.concat([df_train , df_test])


# In[187]:


df.head()


# In[188]:


df.shape


# In[189]:


df.info()


# In[190]:


#df['Date_of_Journey'].str.split('/').str[2] ---> Checking how date can return day , month and year


# In[191]:


#Converting Price float to int

df['Date'] = df['Date_of_Journey'].str.split('/').str[0]
df['Month'] = df['Date_of_Journey'].str.split('/').str[1]
df['Year'] = df['Date_of_Journey'].str.split('/').str[2]


# In[192]:


df.head()


# In[193]:


df.info()


# In[194]:


df['Date'] = df['Date'].astype(int)
df['Month'] = df['Month'].astype(int)
df['Year'] = df['Year'].astype(int)


# In[195]:


df.info()


# In[196]:


df.drop('Date_of_Journey' , axis =1 , inplace = True)


# In[197]:


df.head(10)


# In[198]:


df['Arrival_Time'].str.split(' ').str[0]


# In[199]:


df['Arrival_Time'] = df['Arrival_Time'].str.split(' ').str[0]


# In[200]:


df.head(10)


# In[201]:


df.isnull().sum()


# In[202]:


df['Arrival_Time'].str.split(':').str[0]


# In[203]:


df['Arrival_Hour'] = df['Arrival_Time'].str.split(':').str[0]
df['Arrival_Min'] = df['Arrival_Time'].str.split(':').str[1]


# In[204]:


df.head(10)


# In[205]:


df['Arrival_Hour'] = df['Arrival_Hour'].astype(int)
df['Arrival_Min'] = df['Arrival_Min'].astype(int)


# In[206]:


df.info()


# In[207]:


df.drop('Arrival_Time' , axis =1 , inplace=True)


# In[208]:


df.head()


# In[209]:


df['Dep_Time'].str.split(':').str[0]


# In[210]:


df['Dep_Hour'] = df['Dep_Time'].str.split(':').str[0]
df['Dep_Min'] = df['Dep_Time'].str.split(':').str[1]


# In[211]:


df.drop('Dep_Time' ,axis = 1 , inplace= True)


# In[212]:


df.head()


# In[213]:


df.info()


# In[214]:


df['Dep_Hour'] = df['Dep_Hour'].astype(int)
df['Dep_Min'] = df['Dep_Min'].astype(int)


# In[215]:


df.info()


# In[216]:


df['Total_Stops'].unique()


# In[217]:


df['Total_Stops'] = df['Total_Stops'].map({'non-stop':0 ,'1 stop':1, '2 stops':2 , '3 stops':3 , '4 stops':4 , 'nan':1 })


# In[218]:


df.head()


# In[219]:


df.info()


# In[220]:


df['Total_Stops'].isnull().sum()


# In[ ]:


df['Duration'] = 

