#!/usr/bin/env python
# coding: utf-8

# 
# # Brands Stores Carry
# 
# *This will demonstrate an example of a zip() function. It takes in iterables as arguments and returns an iterator. This iterator generates a series of tuples containing elements from each iterable*
# 

# In[3]:



brand_names = ("Gucci", "Prada", "Xhiliration", "Theory", "Sketchers")
stores = ("Neiman Marcus", "Saks Fifth Avenue", "Target", "Nordstrom", "Payless")

where_to_buy_what = zip(brand_names, stores)

for (a,b) in where_to_buy_what:
    print (a,b)


# *This shows a variety of stores and a sample of the brands they carry*
# 

# **It also showcase a situation in which zip() could be useful**

# In[ ]:




