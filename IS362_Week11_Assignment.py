#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Your task is to choose one of the New York Times APIs, construct an interface in Python to read in the JSON data, and
# transform it into a pandas DataFram

import requests
import json
import pandas as pd

json_link = requests.get('https://api.nytimes.com/svc/books/v3/lists/names.json?api-key=WYH94Zu4p0jdENRNBOO6lGTCUgk5GSqL').text

# print(json)

response_info = json.loads(json_link)

# print(response_info)
# type(response_info)

results = response_info['results']
# print(results)

book_list = []
for book_info in response_info['results']:
 book_list.append([book_info['list_name'], book_info['newest_published_date']])

# print(book_list)

book_df = pd.DataFrame(data=book_list, columns=['List Name', 'Recent Publishing Date'])
top_ten = book_df.head(10)

print(top_ten)


# In[ ]:





# In[ ]:




