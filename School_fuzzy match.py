#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# In[2]:


data = pd.read_stata('school_data.dta')
school = pd.read_excel('Final School scrape.xls')


# In[3]:


print(data)


# In[4]:


print(data[data['distname']=='hyderbad'])
print(data[data['blockname']=='chennai'])
print(data[data['cluster_name']=='chennai'])
print(data[data['village_name']=='chennai'])


# In[5]:


print(data['distname'].unique())


# In[6]:


school = school.drop_duplicates()
print(len(school))
school= school.dropna()
print(len(school))


# In[7]:


choices = list(data['distname'].unique())


# In[8]:


possible=[]
success=[]
for i in school['City']:
    print(len(possible),i)
    ans=process.extractOne(i, choices)
    if ans[1]>92:
        possible.append(ans[0])
        success.append(ans[0])
    else:
        possible.append('No Match')


# In[9]:


print(len(possible))
print(len(success))


# In[10]:


school['city_stat']=possible


# In[11]:


print(school[school['city_stat']=='No Match']['City'].unique())
## mumbai + banglore 330
## 1566 school sample


# In[12]:


#### Reference #######
merg_school=(school[school['city_stat']!='No Match'])


# In[13]:


clean=[]
for i in merg_school['Name']:
    print(i,i.split(',')[0])
    clean.append(i.split(',')[0])


# In[14]:


merg_school['clean_name']=clean


# In[15]:


print(merg_school)


# In[16]:


count=0
for i in merg_school.index:
    name=(merg_school.loc[i,'clean_name'])
    city=(merg_school.loc[i,'city_stat'])
    if name == 'DPS':
        name = 'delhi public school'
        choices = list(data[data['distname']==city]['schname'].unique())
        ans=process.extractOne(name, choices)
        if ans[1]>92:
            merg_school.loc[i,'merged_name']=ans[0]
            print(merg_school.loc[i,'clean_name'],ans[0])
            count=count+1
        else:
            merg_school.loc[i,'merged_name']='NaN'
            print(merg_school.loc[i,'clean_name'],'No Match')
    else:
        choices = list(data[data['distname']==city]['schname'].unique())
        ans=process.extractOne(name, choices)
        if ans[1]>92:
            merg_school.loc[i,'merged_name']=ans[0]
            print(merg_school.loc[i,'clean_name'],ans[0])
            count=count+1
        else:
            merg_school.loc[i,'merged_name']='NaN'
            print(merg_school.loc[i,'clean_name'],'No Match')


# In[18]:


print(merg_school)


# In[43]:


'Navi Mumbai' 'Mumbai'
'Delhi'
'Greater Noida'
'Noida'
'Bengaluru'


# In[20]:


print(school.columns)
print(merg_school.columns)


# 

# In[62]:


mumb = school[school['City'].isin(['Navi Mumbai','Mumbai'])]
match_mum=data[data['distname'].isin([ 'mumbai (suburban)','mumbai ii'])]
clean_m=[]
for i in mumb['Name']:
    #print(i,i.split(',')[0])
    clean_m.append(i.split(',')[0])
mumb['clean_name']=clean_m
count_m=0
choices = match_mum['schname'].unique()

for i in mumb.index:
    print(i)
    name=(mumb.loc[i,'clean_name'])
    ans=process.extractOne(name, choices)
    if ans[1]>92:
            mumb.loc[i,'merged_name']=ans[0]
            print(mumb.loc[i,'clean_name'],ans[0])
            count_m=count_m+1
    else:
            mumb.loc[i,'merged_name']='NaN'
            print(mumb.loc[i,'clean_name'],'No Match')


# In[44]:


beng = school[school['City'].isin(['Bengaluru'])]
match_beng=data[data['distname'].isin(['bengaluru u south','bengaluru rural'  ,'bengaluru u north'])]
clean_b=[]
for i in beng['Name']:
    #print(i,i.split(',')[0])
    clean_b.append(i.split(',')[0])
beng['clean_name']=clean_b
count_b=0
choices = match_beng['schname'].unique()

for i in beng.index:
    #print(i)
    name=(beng.loc[i,'clean_name'])
    ans=process.extractOne(name, choices)
    if ans[1]>92:
            beng.loc[i,'merged_name']=ans[0]
            print(beng.loc[i,'clean_name'],ans[0])
            count_b=count_b+1
    else:
            beng.loc[i,'merged_name']='NaN'
            print(beng.loc[i,'clean_name'],'No Match')


# In[48]:


delh = school[school['City'].isin(['Delhi'])]
match_delh=data[data['distname'].isin(['north west delhi',
 'north delhi', 'north east delhi', 'east delhi', 'new delhi', 'central delhi'
 ,'west delhi', 'south west delhi' ,'south delhi'])]
clean_d=[]
for i in delh['Name']:
    #print(i,i.split(',')[0])
    clean_d.append(i.split(',')[0])
delh['clean_name']=clean_d
count_d=0
choices = match_delh['schname'].unique()

for i in delh.index:
    #print(i)
    name=(delh.loc[i,'Name'])
    ans=process.extractOne(name, choices)
    if ans[1]>92:
            delh.loc[i,'merged_name']=ans[0]
            print(delh.loc[i,'Name'],ans[0])
            count_d=count_d+1
    else:
            delh.loc[i,'merged_name']='NaN'
            print(delh.loc[i,'Name'],'No Match')


# In[53]:


chen = school[school['City'].isin(['Chennai'])]
match_chen=data[data['distname'].isin(['tamil nadu'])]
clean_c=[]
for i in chen['Name']:
    #print(i,i.split(',')[0])
    clean_c.append(i.split(',')[0])
chen['clean_name']=clean_c
count_c=0
choices = match_chen['schname'].unique()

for i in chen.index:
    #print(i)
    name=(chen.loc[i,'clean_name'])
    ans=process.extractOne(name, choices)
    if ans[1]>92:
            chen.loc[i,'merged_name']=ans[0]
            print(chen.loc[i,'clean_name'],ans[0])
            count_c=count_c+1
    else:
            chen.loc[i,'merged_name']='NaN'
            print(chen.loc[i,'clean_name'],'No Match')


# In[54]:


print(count,count_m,count_b,count_d,count_c)


# In[88]:


beng['city_stat']='Bengaluru'
chen['city_stat']='Chennai'
delh['city_stat']='Delhi'
mumb['city_stat']='Mumbai'


# In[94]:


city_stat=[]
for i in data['distname']:
    if i in ['tamil nadu']:
        city_stat.append('Chennai')
    elif i in ['north west delhi',
 'north delhi', 'north east delhi', 'east delhi', 'new delhi', 'central delhi'
 ,'west delhi', 'south west delhi' ,'south delhi']:
        city_stat.append('Delhi')
    elif i in [['bengaluru u south','bengaluru rural'  ,'bengaluru u north']]:
        city_stat.append('Bengaluru')
    elif i in [ 'mumbai (suburban)','mumbai ii']:
        city_stat.append('Mumbai')
    else:
        city_stat.append(i)
    


# In[96]:


data['city_stat']=city_stat


# In[105]:


a = merg_school.append([mumb,beng,chen,delh])


# In[107]:


final = a[a['merged_name']!='NaN']


# In[110]:


all_final = final.merge(data,left_on=['merged_name','city_stat'],right_on=['schname','city_stat'])


# In[111]:


print(all_final)


# In[112]:


all_final.to_excel('ta_school_merge.xlsx')

