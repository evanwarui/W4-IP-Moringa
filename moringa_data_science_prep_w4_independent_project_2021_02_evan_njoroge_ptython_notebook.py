# -*- coding: utf-8 -*-
"""Moringa_Data_Science_Prep_W4_Independent_Project_2021_02_Evan_Njoroge_Ptython_Notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aFQfNHD7QOEi52TsSUYKWxj_wJMHG6at
"""

# Importing numpy
import numpy as np

# Importing pandas
import pandas as pd

#creating DataFrame form url and checking of forst 10 items

url = 'http://bit.ly/autolib_dataset'

df = pd.read_csv(url, encoding= 'Latin1')

df.head(10)

#Checking info our data.
df.info()

#Checking out our data for claening justifications.

# There were no duplicate instances, reasonable null instances


print(df.isnull().sum()) #completeness check
print('***************************************************')
print(df.duplicated().sum()) #consistency check
print('***************************************************')

#Renaming my colums with two names for consistency to allow dropping unwated columns

df.rename(columns={'Bluecar counter':'Bluecar_counter','Utilib counter':'Utilib_counter','Utilib 1.4 counter': 'Utilib_1.4_counter','Charge Slots':'Charge_Slots','Charging Status':'Charging_Status','Displayed comment':'Displayed_comment','Postal code':'Postal_code','Rental status':'Rental_status','Scheduled at':'Scheduled_at','Station type':'Station_type','Subscription status':'Subscription_status'})

# Check the number of cities in paris
cities = df[df['City'] == 'Paris']
print(cities.count())

print('***************************************************')

# most popular hour of day for picking up a Bluecar in Paris over the month of April 2018
# Overall?

df[(df.City == 'Paris')].groupby('hour')['hour'].count().sort_values(ascending = False).head(1)

#Dropping rows and collumns that i will not require.

df.drop(df.loc[df['Kind']=='CENTER'].index, inplace=True) #droping Rows

df.drop(df.loc[df['Rental status']=='broken'].index, inplace=True) #droping Rows

df.drop(['Displayed comment', 'Scheduled at', 'Slots','minute'], axis =1,inplace  =True) #droping collums
        

df.info()

#To proceed with ansering questions, I will create a new colum with reverese running totaol.

df['Running Difference'] = df['Bluecar counter'].sub(df['Bluecar counter'].shift())
df['Running Difference'].iloc[0] = df['Bluecar counter'].iloc[0]
df['Running Difference']

# What is the most popular hour for returning blue cars?
#This is the time the blue cars increased in count

df[df['Bluecar counter'] < 4].groupby('hour')['hour'].count().sort_values(ascending= False).head(1)

# What postal code is the most popular for picking up Bluecars? Does the most popular station belong to that postal code?

# Overall?


df[(df['Kind'] == 'STATION') & (df['Status'] == 'ok')].groupby('Public name')['Public name'].count().sort_values(ascending= False).nlargest(1)

# What postal code is the most popular for picking up Bluecars? Does the most popular station belong to that postal code?

# At the most popular picking hour?

df[(df['Kind'] == 'STATION') & (df['Status'] == 'ok') & (df['hour'] == 4)].groupby('Public name')['Public name'].count().sort_values(ascending= False).nlargest(1)

#Do the results change if you consider Utilib and Utilib 1.4 instead of Blue cars? 

df['Utilib_Diff'] = df['Utilib counter'].diff() #Calulating the reverese of running total
df['Utilib_Diff'].head()

#most popular hour of the day for picking up an Utilib in the city of Paris over the month of April 2018

df[df['Utilib_Diff'] < 0].groupby('hour')['hour'].count().sort_values(ascending= False).nlargest(1)

#most popular hour for returning cars? Utilib

df[df['Utilib_Diff'] > 0].groupby('hour')['hour'].count().sort_values(ascending= False).nlargest(1)

#Most popular picking hour in relation to Utilib

df[df['Utilib_Diff'] > 0].groupby('hour')['hour'].count().sort_values(ascending= False).nlargest(1)

#What postal code is the most popular for picking up Utilib Counter? Does the most popular station belong to that postal code?

df[(df['Kind'] == 'STATION') & (df['Status'] == 'ok') & (df['hour'] == 5)].groupby('Postal code')['Postal code'].count().sort_values(ascending= False).nlargest(1)

#At the most popular picking hour?
df[(df['Kind'] == 'STATION') & (df['Status'] == 'ok') & (df['hour'] == 4)].groupby('Public name')['Public name'].count().sort_values(ascending= False).nlargest(1)

#most popular postal code for picking up utilib

df[(df['Kind'] == 'STATION') & (df['Status'] == 'ok') & (df['hour'] == 4)].groupby('Postal code')['Postal code'].count().sort_values(ascending= False).nlargest(2)

