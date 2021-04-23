#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import requests
import io

url1 = "https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/weather.csv"
url2 = "https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/planes.csv"
url3 = "https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airports.csv"
url4 = "https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airlines.csv"

weather = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/weather.csv") 
planes = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/planes.csv")
airports = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airports.csv")
airlines = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airlines.csv")

# print(airports)
#Trying to answer Question 1, of all the US cities, New York is definitely the Easternmost city. The tz value of America/NY is -5. 
#Show all the NY values, using the chart with airports

chart_for_East = airports[["name","lon", "tz", "tzone"]]
# print(chart_for_East)

America_East = chart_for_East.loc[chart_for_East['tzone'] == 'America/']
# print(America_East)

top_five_east = chart_for_East.nlargest(6, ["lon"])
# print(top_five_east)

NY_East = chart_for_East.loc[chart_for_East['tz'] == -5]
# print(NY_East)

#Getting the top 5 longitude values, indicating furthest East
top_five_east = NY_East.nlargest(6, ["lon"])
print(top_five_east)


# Easternmost airport is Eastport Municipal Airport (Dillant Hopkins again has NaN for tzone)

# In[21]:


weather = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/weather.csv") 
planes = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/planes.csv")
airports = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airports.csv")
airlines = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airlines.csv")


# QUESTION 2
#Trying to answer Question 2, of all the US cities, New York is definitely the northernnmost city. The tz value of America/NY is -5. 
#Show all the NY values, using the chart with airports

# print(airports)

chart_for_North = airports[["name","lat", "tz", "tzone"]]
# print(chart_for_North)


America_North = chart_for_North.loc[chart_for_North['tzone'] == 'America/']
# print(America_North)

top_five_north = chart_for_North.nlargest(6, ["lat"])
# print(top_five_north)

NY_North = chart_for_North.loc[chart_for_North['tz'] == -5]
# print(NY_North)

#Getting the top 5 latitude values, indicating furthest North
top_five_north = NY_North.nlargest(6, ["lat"])
print(top_five_north)


# Northernmost Airport = Northern Aroostook Regional Airport (Dillant Hopkins has NaN for tzone). 

# In[22]:


weather = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/weather.csv") 
planes = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/planes.csv")
airports = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airports.csv")
airlines = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airlines.csv")

print(weather)


# In[33]:


chart_for_Wind = weather[["origin","year", "month", "day", "wind_speed"]]
# print(chart_for_Wind)

# FEb 12, 2013

NY_wind = chart_for_Wind.loc[chart_for_Wind['month'] == 2]
# print(NY_wind)

NY_wind_day = NY_wind.loc[NY_wind['day'] == 12]
# print(NY_wind_day)

NY_wind_year = NY_wind_day.loc[NY_wind_day['year'] == 2013]
# print(NY_wind_year)

windiest = NY_wind_year.nlargest(6, ["wind_speed"])
print(windiest)


# Windiest airport on Feb 12, 2013 was EWR, Newark Airport

# In[ ]:




