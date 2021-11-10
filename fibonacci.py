#!/usr/bin/env python
# coding: utf-8

# ## Fibonacci series

# In[64]:


n=int(input("Enter the number for fibonaaci series"))
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
        
        


# In[ ]:





# In[ ]:




