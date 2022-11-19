#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("covid_19_india.csv")


# In[3]:


data


# In[6]:


confirmed = data.Confirmed.sum()
confirmed


# In[7]:


cured = data.Cured.sum()
cured


# In[8]:


deaths = data.Deaths.sum()
deaths


# In[9]:


sns.set_style(style='whitegrid')
sns.lineplot(x='Deaths',y='Confirmed',data=data)


# In[10]:


sns.set_style(style='whitegrid')
sns.scatterplot(x='Cured',y='Deaths',hue='State/UnionTerritory',data=data)


# In[13]:


sns.set_style(style='whitegrid')
sns.scatterplot(x='Deaths',y='Cured',data=data)


# In[14]:


sns.displot(data['Deaths'],bins=5)


# In[15]:


sns.pairplot(data)


# In[16]:


sns.kdeplot(data=data,x='Deaths')


# In[17]:


sns.catplot(data=data,x='Cured',kind='box')


# In[20]:


slices = [62, 142, 195]
activities = ['Cured', 'Deaths', 'Confirmed']
cols=['#4C8BE2','#00e061','#fe073a']
exp = [0.2,0.02,0.02]
plt.pie(slices,labels=activities,
        textprops=dict(size=25,color='black'),
        radius=3,
        colors=cols,
        autopct='%2.2f%%',
        explode=exp,
        shadow=True,
        startangle=90)
plt.title('Pie chart\n\n\n\n',color='#4fb4f2',size=40)


# In[36]:


a1 = data.groupby('State/UnionTerritory').sum()
b2 = a1.sort_values('Cured',ascending=False)
c3 = b2[['Sno','Confirmed','Deaths','Cured']].head(10)
c3


# In[38]:


fig = plt.figure(figsize=(15,6))
plt.xticks(rotation=45,fontsize=14) 
plt.plot(c3,'r--o')
plt.legend(['Cured'])
plt.xlabel('State/UnionTerritory')
plt.ylabel('Deaths')
plt.title('State Wise max Cured Data')


# In[39]:


a1 = data.groupby('State/UnionTerritory').sum()
b2 = a1.sort_values('Deaths',ascending=False)
c3 = b2[['Sno','Confirmed','Deaths','Cured']].head(10)
c3


# In[40]:


fig = plt.figure(figsize=(15,6))
plt.xticks(rotation=45,fontsize=14) 
plt.plot(c3,'r--o')
plt.legend(['Deaths'])
plt.xlabel('State/UnionTerritory')
plt.ylabel('Deaths')
plt.title('State Wise max Death Data')


# In[49]:


sns.relplot(data=c3,x='State/UnionTerritory',y='Cured',kind='line',ci=None)
plt.xticks(rotation=45,fontsize=10)
fig = plt.figure(figsize=(15,6))


# In[53]:


d4 = data.groupby('State/UnionTerritory').sum()
e5 = d4.sort_values('Cured',ascending=True) # State wise Data Min deaths
f6 = e5[['Deaths','Confirmed','Cured']].head(10)
f6


# In[56]:


fig = plt.figure(figsize=(15,6))
plt.xticks(rotation=50,fontsize=14) 
plt.plot(f6,'g--o')
plt.legend(['Cured'])
plt.xlabel('State/UnionTerritory')
plt.ylabel('Cured')
plt.title('State Wise Min Cured Graph')


# In[55]:


fig = plt.figure(figsize=(15,6))
plt.xticks(rotation=45,fontsize=14) 
plt.plot(f6,'g--o')
plt.legend(['Deaths'])
plt.xlabel('State/UnionTerritory')
plt.ylabel('Deaths')
plt.title('State Wise Min Deaths Graph')


# In[59]:


fig = plt.figure(figsize=(15,6))
plt.xticks(rotation=45,fontsize=14) 
sns.scatterplot(x='State/UnionTerritory',y='Deaths',hue='Cured',data=f6,color='#ED2226')
plt.title('State Wise Min Deaths and Cured Graph')


# In[ ]:





# In[ ]:




