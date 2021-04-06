#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')

# Read data from file 'filename.csv' 
# Control delimiters, rows, column names with read_csv 
# data = pd.read_csv("auto_mpg.data") 
# print (data)

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
data = pd.read_csv(URL, delimiter= r"\s+") 
data.columns = ["Mpg", "Cylinders", "Displacement", "Horsepower", "Weight", "Acceleration", "Model Year", "Origin", "Car Name"]
#print(data)

data['Horsepower'].replace('?', np.NaN)
data_in_numeric = data['Horsepower'].apply(pd.to_numeric, errors='coerce')
#print(data_in_numeric)


data.loc[data['Origin'] == 1, 'Country Origin'] = 'USA'  
data.loc[data['Origin'] == 2, 'Country Origin'] = 'Asia'  
data.loc[data['Origin'] == 3, 'Country Origin'] = 'Europe'  

#print(data)

fig, ax = plt.subplots()
ax.bar(data.index, data["Cylinders"])
plt.show()


scatter_plot = pd.DataFrame(data)
scatter_plot.plot.scatter(x = "Horsepower", y = "Weight")


# Apply the default theme
sns.set_theme()

# Create a visualization
sns.stripplot(
    data=data,
    x="Country Origin", y="Mpg")


# In[ ]:


#The question that this answers: Which country of origin produces cars with the highest MPG. Answer = Europe


# In[ ]:





# In[ ]:




