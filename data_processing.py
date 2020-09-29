#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd

df = pd.read_excel (r'instaCaptions.xlsx')
print (df.iloc[:,0])


# In[81]:


from collections import Counter
Captions=df.iloc[:,0]#.tolist()
#split_it = str(Captions).split() 
#Counter = Counter(split_it)
#most_occur = Counter.most_common(4)
#print(split_it)


# In[82]:




# In[88]:


from nltk.tokenize import TweetTokenizer
import nltk
nltk.download('averaged_perceptron_tagger')
tweet_tokenizer = TweetTokenizer()
tokens = []
total_tokens=0
WordType=[]
for i in range(0,len(Captions)):
    print(nltk.pos_tag(tweet_tokenizer.tokenize(Captions[i])))
    total_tokens=total_tokens+len(set(tweet_tokenizer.tokenize(Captions[i])))-2
    tokens.append(tweet_tokenizer.tokenize(Captions[i]))
    WordType.append(nltk.pos_tag(tweet_tokenizer.tokenize(Captions[i])))
    


# In[89]:


print("Total tokens "+str(total_tokens))
print("avg tokens per caption  " +str(total_tokens/(len(Captions))))


# In[ ]:




