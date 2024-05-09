#!/usr/bin/env python
# coding: utf-8

# In[1]:


# conditional statement
# decision => work


# In[2]:


print("hey")


# In[3]:


# if-else
# osa-gjui-hxb
'''
if(condition):
    statement



'''


# In[9]:


age=19
if(age==18):
    print("age is 18")
else:
    print("condition is false")


# In[11]:


city="Jaipur"
if(city=="jaipur"):
    print("city is correct")
else:
    print("city is incorrect")


# In[15]:


# 10 => "Hello"
# 15 => "hello user"

x=15
if(x==10):
    print("hello")
else:
    print("condition is false")

if(x==15):
    print("hello user")
else:
    print("condition is false")


# In[17]:


x=16
if(x==10):
    print("hello")
elif(x==15):
    print("hello")
else:
    print("condition is false")


# In[18]:


# x--10  => hello     x==15  "hello user"
# x==10   x==15    => hello


# In[24]:


x=12
if(x==10  or x==15):
    print("hello")
else:
    print("condition is false")
    
'''
Q1 take 3 number and find out the minimum
Q2 take a number and check on following conditions
- in case number is greater than 60 print average
- in case number is greater than 75 print Good
- in case number is greater than 85 print excellent
- in case number is greater than 95 print brilliant
otherwise FAIL
'''


# In[26]:


'''
Q1 take 3 number and find out the minimum
Q2 take a number and check on following conditions
- in case number is greater than 60 print average
- in case number is greater than 75 print Good
- in case number is greater than 85 print excellent
- in case number is greater than 95 print brilliant
otherwise FAIL


Q3
input user and we need to calculate the total amount
10 unit => 50 rs
20 => 20rs
10 => 10rs
other unit  => 5

100     =>    500+400+100+300
90

Q4 
Take a variable with any value and check if the number is divisible by
by 6
(6 divisible  : divided by  2 and 3 both )

Q5 
If a user has given me an input 1 => January
2=> february  and upto  12 => December


1) keyword vs identifier
2) What is namespace in Python
'''



# In[27]:


# nested if-else
#  age>18,   city


# In[29]:


age=22
city="Jaipur"

if(age>=18):
    print("Eligible for voting")
    if(city=="Jaipur"):
        print("I can vote")
    else:
        print("Not from Jaipur")
else:
    print("can't vote")

