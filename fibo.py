#!/usr/bin/env python
# coding: utf-8

# ## Fibonacci series

# In[65]:


n=10
a=0
b=1
for i in range(0,n):
    if(i<=1):
        fib=i
    else:
        fib=a+b
        a=b
        b=fib
    print(fib)
        
        

