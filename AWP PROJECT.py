#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


data = pd.read_csv("covid_19_india.csv")


# In[4]:


data


# In[5]:


data.head()


# In[6]:


states_confirmed = data.groupby('State/UnionTerritory').Confirmed.sum()
states_confirmed


# In[7]:


states_deaths = data.groupby('State/UnionTerritory').Deaths.sum()

states_deaths


# In[9]:


states_cured = data.groupby('State/UnionTerritory').Cured.sum()            
states_cured


# In[10]:


data['Confirmed'].sum()             


# In[11]:


data['Deaths'].sum()                  


# In[12]:


data['Cured'].sum()                    


# In[14]:


maharashtra = data[data['State/UnionTerritory'] == 'Maharashtra']    

maharashtra


# In[16]:


total_quantity = data.groupby('State/UnionTerritory').agg(['count','max','min','sum'])    
total_quantity


# In[19]:


data['Date'] = pd.to_datetime(data['Date']).dt.date
data['Time'] = pd.to_datetime(data['Date']).dt.time


# In[20]:


date_confirmed = data.groupby('Date').Confirmed.sum()
date_confirmed 


# In[21]:


date_death = data.groupby('Date').Deaths.sum()
date_death


# In[22]:


date_cured = data.groupby('Date').Cured.sum()

date_cured


# In[24]:


confirmed_indiannational = data.groupby('State/UnionTerritory').ConfirmedIndianNational.sum()
confirmed_indiannational


# In[25]:


confirmed_foreignnational = data.groupby('State/UnionTerritory').ConfirmedForeignNational.sum()

confirmed_foreignnational


# In[27]:


data.min()


# In[28]:


data.max()


# In[29]:


pd.DataFrame(data.describe())


# In[30]:


from datetime import date


# In[31]:


state_data =data.groupby(['State/UnionTerritory'])


# In[32]:


state_data


# In[ ]:





# In[37]:


data.head()


# In[38]:


data.tail()


# In[ ]:





# In[ ]:




