#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


start = 1
stop = 10000
length = 20


# In[3]:


#create a list in the range(start,stop) with the length--Version1
def random_int_list(start, stop, length):
    lenth=int(abs(length))
    random_list=[]
    if start <= stop:
        start,stop=(int(start),int (stop))
    else:
        start,stop=(int(stop),int(start))      
    for i in range(lenth):
        random_list.append(random.randint(start,stop))
    return random_list


# In[4]:


random_list=random_int_list(start,stop,length)
print(random_list)


# In[7]:


random_list=list(set(random_list)) #clean repeat data
#print(random_list)
random_list.sort() #get a sort data list
#print(random_list)


# In[ ]:


#another way to sort data
# random_list=sorted(random_list)
# print(random_list)
# sorted 有返回值，sort没有返回值


# In[8]:


item=random.sample(random_list,1) #get a list only has one item-->item[0]
#print(item)


# In[13]:


#binary tree demo (below)
def binary_tree(random_list,item):
    low=0
    high=len(random_list)-1
    while low<high: 
        mid=int((low+high)/2) #mid must be an int
        guess=random_list[mid]
        if guess == item[0]: 
            return mid
        if guess < item[0]:
            low=mid+1
        else:
            high=mid-1
    return None


# In[12]:


result=binary_tree(random_list,item)
print(result)


# In[ ]:




