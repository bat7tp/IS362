#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
df = pd.read_csv(r"C:/Users/batsh/Documents/CUNY/IS362/Week 7 Assignment.csv")

print(df.head())

av_row = df.mean(axis=1)
print (av_row)

#The Black Widow Movie has the highest Average Rating


# In[ ]:




