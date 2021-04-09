#!/usr/bin/env python
# coding: utf-8

# In[28]:


import sqlite3
import pandas as pd
conn = sqlite3.connect(r"C:\Users\batsh\Downloads\chinook-database-master\chinook-database-master\ChinookDatabase\DataSources\Chinook_Sqlite.sqlite")
cursor = conn.cursor()

#cursor.execute("SELECT * FROM Album")
# result = cursor.fetchall()
# print(result)

df1 = pd.read_sql_query("SELECT * FROM Album", conn)
# print(df1.head(5))

df2 = pd.read_sql_query("SELECT * FROM Customer", conn)
# print(df2.head(5))

df3 = pd.read_sql_query("SELECT * FROM Track", conn)
# print(df3.head(5))

df4 = pd.read_sql_query("SELECT * FROM Invoice", conn)
# print(df4.head(5))

df5 = pd.read_sql_query("SELECT * FROM InvoiceLine", conn)
# print(df5.head(5))


#JOIN THE TABLES
df_joined1 = pd.merge(df1, df3, on='AlbumId', how='outer')
# print(df_joined1)

df_joined2 = pd.merge(df_joined1, df5, on='TrackId', how='outer')
# print(df_joined2)

df_joined3 = pd.merge(df_joined2, df4, on='InvoiceId', how='outer')
# print(df_joined3)

all_joined = pd.merge(df_joined3, df2, on='CustomerId', how='outer')
# print(all_joined)

#Drop the unwanted columns
dfjoined = all_joined.drop(['SupportRepId','Fax','Phone', 'PostalCode', 'Email', 'Country', 'State', 'City', 'Address', 'Company', 'BillingPostalCode', 'Bytes', 'Milliseconds', 'Composer','GenreId', 'MediaTypeId', 'TrackId', 'ArtistId', 'AlbumId', 'BillingCountry', 'Total','BillingState', 'BillingCity', 'BillingAddress', 'InvoiceDate', 'CustomerId', 'Quantity', 'UnitPrice_y', 'InvoiceId', 'InvoiceLineId','UnitPrice_x' ],axis=1)
# print(dfjoined)

#Sort the table

sorted_table = dfjoined.sort_values(by='LastName', ascending=True)
print(sorted_table.head(5))


# In[ ]:




