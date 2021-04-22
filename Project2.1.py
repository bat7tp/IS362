#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd

income_df = pd.read_csv("/Users/batsh/Documents/CUNY/IS362/Week5part1relinc.csv")

# print(income_df)

new_income_df = income_df.rename(columns={'<10k' : 'Number of People with an Income of <10k','10-20k' : 'Number of People with an Income of 10-20k','20-30k' : 'Number of People with an Income of 20-30k', '30-40k' : 'Number of People with an Income of 30-40k' , '40-50k' : 'Number of People with an Income of 40-50k', '50-75k' : 'Number of People with an Income of 50-75k', '75-100k' : 'Number of People with an Income of 75-100k', '100-150k' : 'Number of People with an Income of 100-150k', '>150k' : 'Number of People with an Income of >150k' })
print(new_income_df)


# In[12]:


import pandas as pd
corona_df = pd.read_csv('/Users/batsh/Documents/CUNY/IS362/utfcoronadata1.csv')
print(corona_df)


# In[ ]:




