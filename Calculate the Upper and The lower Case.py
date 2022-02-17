#!/usr/bin/env python
# coding: utf-8

# In[2]:


def string(s):
    a={"upper_case":0,"lower_case":0}
    for u in s:
        if u.isupper():
            a["upper_case"]+=1
        elif u.islower():
            a["lower_case"]+=1
    print("No. of Upper case characters : ",a["upper_case"])
    print("No. of Lower case Characters : ",a["lower_case"])
    
string("The quick Brow Fox")

