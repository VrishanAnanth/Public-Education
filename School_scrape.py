#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy
import time
import pandas as pd
from scrapy.crawler import CrawlerProcess
import numpy as np


# In[2]:


links= ['https://www.educationworld.in/ew-india-school-rankings-2020-21/?school=Co-ed%20Day','https://www.educationworld.in/ew-india-school-rankings-2020-21/?school=Co-ed%20Day&range=101','https://www.educationworld.in/ew-india-school-rankings-2020-21/?school=Co-ed%20Day&range=401','https://www.educationworld.in/ew-india-school-rankings-2020-21/?school=Co-ed%20Day&range=701']
df = pd.DataFrame(columns= ['2019','2020','Name','City','State','Score','Show'])
s = []


# In[3]:



class SchoolsScrape(scrapy.Spider):
    name='school_scraper'
    
    def start_requests(self):
        for link in links:
            print(link)
            yield scrapy.Request(url=link,callback=self.get_school)
        
    def get_school(self,response):
        data = response.xpath('//tbody//td//text()').extract()
        print(data)
        s.append(data)
       


# In[4]:


process= CrawlerProcess()
process.crawl(SchoolsScrape)
process.start()


# In[5]:


data=(s[0])
for i in s:
    print(len(i))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[7]:


print(s[1][210:215])
g_list =s[1]
print(len(g_list))
del g_list[210:215]
print(len(g_list))


# In[11]:


a = np.array(g_list)
final = np.reshape(a,(-1,7))
#print(final)
check= pd.DataFrame(final)
print(len(check))


# In[18]:


data_sets = [s[0],s[2],s[3]]
for i in data_sets:
    ab = np.array(i)
    fin = np.reshape(ab,(-1,7))
    datf = pd.DataFrame(fin)
    print(len(check))
    check=check.append(datf)
    print(len(check))


# In[19]:


final_data = check.drop_duplicates()


# In[23]:


final_data.columns=['2019_rank','2020_rank','Name','City','State','Score','Show']
print(final_data)


# In[24]:


print(final_data[final_data['City']=='Hyderabad'])


# In[25]:


final_data.to_excel('coed_day.xlsx')

