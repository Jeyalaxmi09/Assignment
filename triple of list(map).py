#!/usr/bin/env python
# coding: utf-8

# In[1]:


nums = (1, 2, 3, 4, 5, 6, 7) 
print("list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("Triple of list :")
print(list(result))

