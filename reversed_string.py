#!/usr/bin/env python
# coding: utf-8

# In[1]:


def reversed_string(str):  
    str1 = ""   
    for i in str:
        str1 = i +str1
    return str1    
     
str = input("Enter a string") 
print("The original string is: ",str)  
print("The reverse string is",reversed_string(str))  

