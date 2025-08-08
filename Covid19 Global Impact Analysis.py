#!/usr/bin/env python
# coding: utf-8

# # COVID-19:Global Impact Analysis

# # Import Libraries and Load Dataset

# In[27]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


df = pd.read_csv('owid-covid-data.csv', parse_dates=['date'])


# In[3]:


cols = [
    'date', 'location', 'continent', 'population',
    'total_cases', 'new_cases', 'total_cases_per_million', 'new_cases_per_million',
    'total_deaths', 'new_deaths', 'total_deaths_per_million', 'new_deaths_per_million',
    'total_tests', 'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand',
    'positive_rate', 'total_vaccinations', 'people_vaccinated',
    'people_fully_vaccinated', 'new_vaccinations', 'stringency_index'
]

df = df[cols]


# In[4]:


df.head()


# In[5]:


df.describe()


# In[6]:


df.info()


#  # Data Cleaning & Transformation

# In[7]:


df.isnull().sum()


# In[8]:


df['date'] = pd.to_datetime(df['date'])


# In[9]:


df.fillna(0, inplace=True)


# In[25]:


df['vaccination_rate'] = (df['people_fully_vaccinated'] / df['population']) * 100


# In[11]:


df['deaths_per_100k'] = (df['total_deaths'] / df['population']) * 100000


# In[12]:


df.tail(10)


# # Graphical Data Analysis

# In[13]:


top_countries = df.groupby('location')['total_cases'].max().nlargest(10).index
df_top = df[df['location'].isin(top_countries)]

plt.figure(figsize=(14,6))
for country in top_countries:
    subset = df_top[df_top['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)
plt.legend()
plt.title("Total COVID-19 Cases Over Time (Top 10 Countries)")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[14]:


cumulative = df.groupby(['date', 'continent'])['total_deaths'].sum().reset_index()
pivoted = cumulative.pivot(index='date', columns='continent', values='total_deaths').fillna(0)
pivoted.plot.area(stacked=True, figsize=(12,6), alpha=0.7)
plt.title("Cumulative Deaths by Continent Over Time")
plt.ylabel("Total Deaths")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[15]:


plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='stringency_index', bins=30, kde=True)
plt.title('Distribution of Stringency Index')
plt.xlabel('Stringency Index')
plt.ylabel('Frequency')
plt.show()


# In[28]:


fig = px.line(
    df[df['location'] == 'United States'],
    x='date', y='new_cases',
    hover_data=['new_deaths', 'new_vaccinations'],
    title='US COVID-19 New Cases Timeline'
)
fig.show()


# In[18]:


top_deaths = df[['location', 'deaths_per_100k']].nlargest(10, 'deaths_per_100k').sort_values('deaths_per_100k')

plt.figure(figsize=(10,6))
plt.hlines(y=top_deaths['location'], xmin=0, xmax=top_deaths['deaths_per_100k'], color='skyblue')
plt.plot(top_deaths['deaths_per_100k'], top_deaths['location'], "o")
plt.title('Top 10 Countries by Death Rate (per 100k)')
plt.xlabel('Deaths per 100k')
plt.tight_layout()
plt.show()


# In[29]:


top_vax = df[['location', 'vaccination_rate']].dropna().sort_values('vaccination_rate', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=top_vax, x='vaccination_rate', y='location', palette='viridis')
plt.title('Top 10 Countries by Vaccination Rate')
plt.xlabel('Vaccination Rate (%)')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

