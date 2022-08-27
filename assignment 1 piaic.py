#!/usr/bin/env python
# coding: utf-8

# In[1]:


nationality = ("I am a pakistani")
print(nationality)


# In[3]:


quaid_quote = ("There is no power on earth that can undo Pakistan")
print(quaid_quote)


# In[4]:


radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius**2
print("The area of the circle is", area)


# In[5]:


num = int(input("Enter a number:"))
if num > 0:
    print(num, "is positive")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is negative")


# In[6]:


Vowels = input("Enter a vowel:")
if Vowels in ('a','e','i','o','u','A','E','I','O','U'):
    print(Vowels, "is a vowel")
else:
    print(Vowels, "is not a vowel it's a consonant")


# In[7]:


Vowels = input("Enter a vowel:")
if Vowels in ('a','e','i','o','u','A','E','I','O','U'):
    print(Vowels, "is a vowel")
else:
    print(Vowels, "is not a vowel it's a consonant")


# In[10]:


names = ['salman', 'hanbal', 'ayeza', 'ashhad']
for i in names:
    print(i)


# In[11]:


for i in names:
    print(i , "is very good person")


# In[7]:


favourite = ["pizza", "burger", "kabab", "nihari", 'biryani', 'qorma', ' karahi', ' tikka', "broast"]

print("Three first dishes are: " ,favourite)
print("Three middle dishes are: ", favourite)
print("The last three dishes are: ", favourite)


# In[9]:


friend_foods =["shawarma", "burger", "kababs", "broast", "nihari", 'pulao', 'qorma', ' karahi', ' tikka']
friend_foods.append("mandi")
print(friend_foods)


# In[10]:


print("list one is :" ,favourite)
print("list two is :", friend_foods)


# In[11]:


for i in favourite:
    
    print("My favourite food is  ", i)


# In[12]:


for i in friend_foods:
    print("My friend's favourite food is  ", i)


# In[ ]:




