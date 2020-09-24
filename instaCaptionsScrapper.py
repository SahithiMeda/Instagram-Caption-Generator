#!/usr/bin/env python
# coding: utf-8

# In[93]:


import requests
from bs4 import BeautifulSoup
import json 
import ast 



# In[108]:


page = requests.get("https://www.instagram.com/p/CFh-2m_M2Ks/")
page


# In[ ]:





# In[ ]:





# In[ ]:





# In[100]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[109]:


print(soup.find_all("title")[0].get_text().partition(':')[2] )


# In[ ]:




