#!/usr/bin/env python
# coding: utf-8

# In[40]:



import requests
import pandas as pd
import pyodbc

oscar_data = pd.read_csv("/Users/batsh/Documents/IS362 final data stuff.csv")

df = pd.DataFrame(oscar_data)

#print(df)


sel_df = df[["Year","Award", "Winner", "Film", "Name"]]

#print(sel_df)

specific = sel_df.loc[(sel_df['Award'] == 'Film Editing') | (sel_df['Award'] == 'Best Picture')]

#print(specific)

category_df = pd.DataFrame(specific)

#print(category_df)

#1962 was the first year to have a best picture award category. All years prior  are not relevant for discovering connection between the two categories

winners = category_df.loc[(category_df['Winner'] == 1.0) & (category_df['Year'] >= '1962') ]

#print(winners)

top_ten = winners.head(10)
print(top_ten)


# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=RON\SQLEXPRESS;'
#                       'Database=TestDB;'
#                       'Trusted_Connection=yes;')
# cursor = conn.cursor()


# In[ ]:




