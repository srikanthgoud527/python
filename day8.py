#!/usr/bin/env python
# coding: utf-8

# In[7]:


def binarysearch(a,lindex,rindex,taritem):
    while lindex<=rindex:
        mindex=lindex+(rindex-lindex)//2;
        if a[mindex]==taritem :
            return mindex
        if a[mindex]>taritem:
            rindex=mindex-1
        else:
            lindex=mindex+1
    return -1
list1=[1,4,9,15,25,45,57,88,98]
res =binarysearch(list1,0,8,4)
if res!=-1:
    print("item is  found")
else:
    print("item is not found")


# In[1]:


def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            
    for i in range(len(a)):
        print(a[i],end=" ")
        
list1=[19,25,1,18,3]
bubblesort(list1)


# In[2]:


list1=[10,12,3,5,6]
list1.sort()
print(list1)


# In[3]:


# creating a string
str ="appiction"
print(str)
str1 ='application'
print(str1)


# In[7]:


# creating a string
str ="appiction"
print(str)
print("str[0]=",str[0])
print("str[1]=",str[1])
print("str[-1]=",str[-1])
print("str[-3]=",str[-3])
print("str[1:5]=",str[1:5])
print("str[:5]=",str[:5])
print("str[5:-2]=",str[5:-2])
print("str[::-1]=",str[::-1])


# In[8]:


def countofchars(str):
           return len(str)
countofchars("application")


# In[10]:


def countuppercase(str):
    count=0
    return count
print(countuppercase("Application "))
print(countuppercase("tesT"))


# In[21]:


def countuppercase(str):
    count=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=65 and ord(lst[x])<=90:
            count=count+1
    return count
print(countuppercase("AAApplication"))
print(countuppercase("tesGGt"))


# In[25]:


def printdigits(str):
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            print(lst[x],end="")
    
print(printdigits("applicationA1889"))#1889


# In[26]:


def sumofdigits(str):
    sum=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            sum=sum+ord(lst[x])-48;
            
    return sum
sumofdigits("applications1889")


# In[30]:


def sumonlyevendigits(str):
    sum=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            if(ord(lst[x])%2==0):
                sum=sum+ord(lst[x])-48;
            
    return sum
print(sumonlyevendigits("applications1889"))


# In[ ]:




