#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt


# In[50]:


import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[51]:


df1 = pd.read_csv('singers_gender (1).csv', encoding= 'latin1') 
print(df1)


# In[52]:


df1= df1.dropna(subset= ['gender'])
#dropping any entries with no value


# In[53]:


df1=df1.rename(columns= {'artist':'Perfomer'})
#renaming the artist column as performer
#column now matches the billdboard hot 100 data set


# In[54]:


df1['category'].value_counts()
#list of types of artists, including ethnicity and music style


# In[55]:


df1=df1.drop(['category'], axis=1)
#after looking at category (just for fun), i dropped it because it was not needed


# In[56]:


df2 = pd.read_csv('billboardHotWeekly.csv') 
print(df2)


# In[57]:


df2.drop(['SongID', 'PreviousWeekPosition', 'PeakPosition', 'Week Position', 'Instance', 'url'], axis=1)
#dropping the columns i won't be working with


# In[58]:


df1['gender'].value_counts()


# In[59]:



gender = [15236,7941]

my_labels = 'male','female',
my_colors = ['lightblue','lightsteelblue']
my_explode = (0.1, 0)
plt.pie(gender, labels=my_labels, autopct='%1.1f%%', startangle=15, shadow = True, colors=my_colors, explode=my_explode)
plt.title('gender in the billboard hot 100')
plt.axis('equal')
plt.show()


# In[38]:


df1['Performer'].isin(df2['Performer']).valuecounts()


# In[36]:


df = pd.merge(df1,
                 df2[['Performer', 'WeekID']],
                 on='Performer')
df.head()
#merge the two dataframes into one using Performer as the common value


# In[ ]:


ax = df.plot.bar(rot=0)


# In[ ]:


print(df)


# In[ ]:




