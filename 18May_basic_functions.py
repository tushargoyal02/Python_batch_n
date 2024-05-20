#!/usr/bin/env python
# coding: utf-8

# In[1]:


# functions
# named block
# block of code  
# logic  => reuse


# In[2]:


'''
datatype  function_name():
    logic
    
# code reuse
# small portion using function => debugging



'''


# In[3]:


'''
def  function():
    logic

'''


# In[4]:


# function declare
def msg():
    print("hello")


# In[8]:


# function calling
msg()
msg()
msg()


# In[11]:


def msg(x):
    print("hello",x)


# In[16]:


msg(10)
msg(20)
msg("hello")


# In[21]:


def msg(x):
    for i in range(0,x):
        print(i)
    
msg(15)


# In[22]:


# 5
def func(x,y):
    if(x%5==0  and y%5==0):
        print("Divisible by 5")
    else:
        print("Not divisble")


# In[26]:


func(10,21)


# In[29]:


func(5,10)


# In[30]:


# x => parameter / formal parametre / informal argument
def func(x):
    print("x value is:",x)
    
# argument / formal argument  / informal parameter
func(10)


# In[31]:


def func(x):
    print("x value is:",x)
    
func(10)


'''
logic to take a argument from the user and check whether 
is a prime number
6
2

'''



# In[38]:


def func(num):
    x=0
    if(num>1):
        for i in range(2, num):
            if(num%i==0):
                x=1
                break
                
        if(x==1):
            print("Not a prime")
        else:
            print("Prime")
                
    
func(12)


# In[39]:


# create a function which will print the following pattern
# based on the number

'''
4
D 10 E 20 F 30 
G 40 H 50
I 60

DEF
GH

68 69 70



'''


# In[46]:


def func(x):
    count=68
    for i in range(1,x+1):
        for j in range(i,x+1):
            print( chr(count) ,end=" ")
            count+=1
        print(" ")
        
func(6)
    


# In[52]:


# create a function which takes 2 value as parameter and find the lcm
# lease common multipler
# 2,8

def lcm(x,y):
    if(x>y):
        greatest=x
    else:
        greatest=y

    while(True):
        if(greatest%x==0  and greatest%y==0):
            print("LCM is ", greatest)
            break
        greatest+=1
        
lcm(12,14)


# In[ ]:


# hcf
#2,4
# 24 7

