#!/usr/bin/env python
# coding: utf-8

# In[156]:


import numpy as np


# In[164]:


#Receive an input from a user
value = input('Please enter value as a: ')

a = range(0,9)

#create a function
def calculate (val):
    if len(val) != 9:
        print ("Not a 3x3 expected matrix value")
        
    #convert to numpy array and reshape to 3x3 matrix     
    num = np.array(val).reshape(3,3)
    result = {"mean": [num.mean(0).tolist(), num.mean(1).tolist(), num.mean()],         
        "variance": [num.var(0).tolist(), num.var(1).tolist(), num.var()],   
        "standard deviation": [num.std(0).tolist(), num.std(1).tolist(), num.std()],
        "max": [num.max(0).tolist(), num.max(1).tolist(), num.max()],
        "min": [num.min(0).tolist(), num.min(1).tolist(), num.min()],
        "sum": [num.sum(0).tolist(), num.sum(1).tolist(), num.sum()]}
    return result
    


# In[165]:


# Call the created function
calculate([i for i in a])

