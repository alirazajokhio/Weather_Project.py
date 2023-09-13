#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_csv(r"E:\Weather data set.csv")


# In[4]:


data


# In[5]:


data.head()


# In[7]:


data.shape


# In[9]:


data.index


# In[10]:


data.columns


# In[11]:


data.dtypes


# In[13]:


data['Weather'].unique()


# In[14]:


data.nunique()


# In[15]:


data.count()


# In[19]:


data['Weather'].value_counts()


# In[21]:


data.info()


# In[ ]:


#Q1: Find all the unique "Wind Speed" values in the data.


# In[42]:


data['Wind Speed_km/h'].unique()


# In[ ]:


#Q2: Find the number of time weather is "exactly clear"


# In[26]:


data.head(2)


# In[41]:


data['Weather'].value_counts()


# In[45]:


#we can also answer it by another two methods,(a) filtering (b) groupby

data[data.Weather == 'Clear']

#now just see the rows, which are equal to 1326. Thats our answer!!


# In[47]:


# using groupby method

data.groupby('Weather').get_group('Clear')

#look at the rows, 1326


# In[48]:


#Q3: Find the number of times when the 'Wind speed' was exactly '4km/hr'

##We will solve it by 3 methods (1) value_counts (2) Groupby (3) Filtering


# In[49]:


data.head(2)


# In[51]:


data['Wind Speed_km/h'].value_counts()


# In[58]:


data.groupby('Wind Speed_km/h').get_group(4)


# In[62]:


data[data['Wind Speed_km/h'] == 4]


# In[63]:


#Q4: Find all the null values in the data


# In[65]:


data.isnull().sum()


# In[66]:


data.notnull().sum()


# In[67]:


#Q5: Rename the column "Weather" in the dataframe to "weather Conditions"


# In[68]:


data.head()


# In[71]:


data.rename(columns = {'Weather' : 'Weather Condition'}) #This is temporary. For permanent change just add ,inlpace = True)


# In[72]:


#What is the average of visibility?


# In[76]:


data.Visibility_km.mean()


# In[ ]:


#Q7: What is the standard deviation of 'Pressure' in this data?


# In[77]:


data.head(2)


# In[78]:


data.Press_kPa.std()


# In[ ]:


#Q8: What is the Variance of 'Relative Humidity' in this data?


# In[79]:


data.head(2)


# In[80]:


data['Rel Hum_%'].var()


# In[ ]:


#Q9: Find all instances when 'Snow' was Recorded.


# In[84]:


data.groupby('Weather').get_group('Snow')


# In[86]:


data[data.Weather == 'Snow']


# In[87]:


data['Weather'].value_counts()


# In[88]:


data[data['Weather'].str.contains('Snow')]


# In[89]:


#Q10: Find all instances when "Wind Speed is above 24" and Visibility is 25'


# In[90]:


data.head(2)


# In[92]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# In[93]:


#Q11: What is the mean value of each column against weather'


# In[94]:


data.head(2)


# In[95]:


data.groupby('Weather').mean()


# In[96]:


#Q12: What is the minimun and maximum value of each column against each 'Weather'


# In[97]:


data.head(2)


# In[98]:


data.groupby('Weather').min()


# In[99]:


data.groupby('Weather').max()


# In[ ]:


#Q13: Show all the records where weather codition is Fog


# In[100]:


data[data['Weather'] == 'Fog']


# In[101]:


#Q14: Find all the instances when 'Weather is Clear and visibility is above 40'.


# In[106]:


data[(data['Weather'] == 'Clear') | (data['Visibility_km'] > 40)]


# In[107]:


#Q15: Find all the instances when:
#A. "Weather is clear" and Relative Humadity is greater than 50'
#or
#"Visibility is above 40"


# In[109]:


data[(data['Weather'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] >40)]

