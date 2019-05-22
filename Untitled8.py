#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
x=np.array([1,2,32,55,5,8,90,4,67,86,6,33,99,21,22,54])
y=np.array([5,7,31,89,9,8,646,7,120,424,8,77,99,34,44,67])
alpha=0.000001
theta0=1
x0=1
theta1=2
import matplotlib.pyplot as plt
plt.scatter(x,y)
for i in range(10000):
    print(theta1)
    theta0,theta1=theta0-(alpha/len(x))*(sum(theta1*x-y)+len(x)*theta0),theta1-(alpha/len(x))*(sum((theta1*x-y)*x.T)+len(x)*theta0)
#important note
    #in case of multipole features the general formula will be:
    #first add xo in the x as 
    #np.insert(x,0,1,axis=1)
    #for i in range(1000):
        #theta=theta-(alpha/len(x))*(theta*x.T-y)*x
print(theta0)
print("23")
t0=np.ones(len(x))
cost=(1/(2*len(x)))*sum((theta1*x-y+t0)*(theta1*x-y+t0))
print(cost)
plt.plot(x,theta1*x+t0)
plt.show()
    

