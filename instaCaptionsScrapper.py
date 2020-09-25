#!/usr/bin/env python
# coding: utf-8

# In[93]:


import requests
from bs4 import BeautifulSoup

my_file = open("Links.txt", "r")
content = my_file.read()
content_list = content.splitlines()
my_file.close()

for i in content_list:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.find_all("title")[0].get_text().partition(':')[2] )




    



