#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import time, urllib.request
import requests
import re
import os
import csv
import json
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# In[58]:


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com/")
#login
time.sleep(5)
username=driver.find_element_by_css_selector("input[name='username']")
password=driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("sirdatadummy")
password.send_keys("Sauter@2022")
login = driver.find_element_by_css_selector("button[type='submit']").click()

time.sleep(10) 
notnow = driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click() 
#Ativar Notificações 
time.sleep(10) 
notnow2 = driver.find_element_by_xpath ("//button[contains(text(), 'Agora não')]").click()

time.sleep(5) 
searchbox=driver.find_element_by_css_selector("input[placeholder='Pesquisar']") 
searchbox.clear() 
searchbox.send_keys("cea_brasil") 
time.sleep(5) 
searchbox.send_keys( Keys.ENTER) 
time.sleep(5) 
searchbox.send_keys(Keys.ENTER)

#Scroll
scrolldown=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;") 
match=False 
while(match==False): 
    last_count = scrolldown 
    time.sleep(5) 
    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;") 
    if last_count==scrolldown: 
        match=True


# In[39]:


# Links das Postagens        
posts = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)

print(posts)


# In[23]:


df = pd.DataFrame(posts, columns=['Link_posts'])
df


# In[24]:


for index, row in df.iterrows():
    print(row['Link_posts'])
    
    


# In[33]:


lista_dataframes = []

for index, row in df.iterrows():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(row['Link_posts'])

    try:

        time.sleep(5)
        username=driver.find_element_by_css_selector("input[name='username']")
        password=driver.find_element_by_css_selector("input[name='password']")
        username.clear()
        password.clear()
        username.send_keys("sirdatadummy")
        password.send_keys("Sauter@2022")
        login = driver.find_element_by_css_selector("button[type='submit']").click()

        time.sleep(10) 
        notnow = driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click() 

        comments = []

        hasLoadMore = True
        while hasLoadMore:
            time.sleep(1)
            try:
                if driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > div.EtaWk > ul > li > div > button > span'):
                    driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > div.EtaWk > ul > li > div > button > span').click()
            except:
                hasLoadMore = False

        users_list = []
        users = driver.find_elements_by_class_name('_6lAjh')
        for user in users:
            users_list.append(user.text)

        i = 0
        texts_list = []
        texts = driver.find_elements_by_class_name('MOdxS')
                                            
        for txt in texts:
            texts_list.append(txt.text)
            i += 1
            comments_count = len(users_list)

        for i in range(1, comments_count):
            user = users_list[i]
            text = texts_list[i]
            comments.append(users_list[i])
            comments.append(texts_list[i])
            # print("User ",user)
            # print("Text ",text)


        dicionario = {'User': users_list,
                    'Text': texts_list,
                    'Link': row['Link_posts']}


        dataframe = pd.DataFrame(dicionario)
        #lista_dataframes.append(dataframe)

        
        dataframe = dataframe.assign(Description_post = dataframe['Text'][0])
        dataframe2 = dataframe[1:]
        lista_dataframes.append(dataframe2)
    
    except:

        comments = []

        hasLoadMore = True
        while hasLoadMore:
            time.sleep(1)
            try:
                if driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > div.EtaWk > ul > li > div > button > span'):
                    driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > div.EtaWk > ul > li > div > button > span').click()
            except:
                hasLoadMore = False

        users_list = []
        users = driver.find_elements_by_class_name('_6lAjh')
        for user in users:
            users_list.append(user.text)

        i = 0
        texts_list = []
        texts = driver.find_elements_by_class_name('MOdxS')
                                            
        for txt in texts:
            texts_list.append(txt.text)
            i += 1
            comments_count = len(users_list)

        for i in range(1, comments_count):
            user = users_list[i]
            text = texts_list[i]
            comments.append(users_list[i])
            comments.append(texts_list[i])
            # print("User ",user)
            # print("Text ",text)


        dicionario = {'User': users_list,
                    'Text': texts_list,
                    'Link': row['Link_posts']}


        dataframe = pd.DataFrame(dicionario)
        #lista_dataframes.append(dataframe)

        dataframe = dataframe.assign(Description_post = dataframe['Text'][0])
        dataframe2 = dataframe[1:]
        lista_dataframes.append(dataframe2)



df_concated =pd.concat(lista_dataframes)
df_concated


# In[12]:


users_list = []
users = driver.find_elements_by_class_name('_6lAjh')
for user in users:
    print(user)
    users_list.append(user.text)

i = 0
texts_list = []
texts = driver.find_elements_by_css_selector('#react-root > section > main > div > div > article > div > div.HP0qD > div > div > div.eo2As > div.EtaWk > ul > li > div > button > div > svg')
for txt in texts:
    texts_list.append(txt.text)
    i += 1
    comments_count = len(users_list)

for i in range(1, comments_count):
    user = users_list[i]
    text = texts_list[i]
    comments.append(users_list[i])
    comments.append(texts_list[i])
    print("User ",user)
    print("Text ",text)
    print()


# In[ ]:




