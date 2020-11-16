
# coding: utf-8

# In[1]:


import random as rd


# In[2]:

#bitonic sort is my special feature in this repository!!!
#bitonic sort is cool as well as difficult to understand
#if you look for detailed explanation, you should check out geeksforgeeks
# https://www.geeksforgeeks.org/bitonic-sort/
#its python version is written in recursion
#which i found it really difficult to understand what the heck it was doing
#so i spent the whole day scratching my head to finish this non-recursive version
#a more straight forward explanation is the visualization from wikipedia
# https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/BitonicSort1.svg/843px-BitonicSort1.svg.png

#enjoy~~~
def bitonic_sort(target):
    
    if len(target)==1:
        return target
    
    i=1
    
    #primary iteration
    while 2**(i-1)<len(target)/2+1:
    
        j=2**i
    
        direction=get_direction(j,len(target))
        
        #secondary iteration
        while j>=2:
            
            #double loop helps us to find out who is comparing with who for each round
            #the sorting order is given by another function called get_direction
            for k in range(0,len(target),j):            
                for l in range(k,k+int(j/2)):
                    
                    if target[l]>target[l+int(j/2)] and \
                    direction[l]==1:
                        target[l],target[l+int(j/2)]=target[l+int(j/2)],target[l]
                        
                    if target[l]<target[l+int(j/2)] and \
                    direction[l]==-1:
                        target[l],target[l+int(j/2)]=target[l+int(j/2)],target[l]
            
            #int is important
            #list indices dont support float
            #when u do /, we get float by default
            j=int(j/2)
     
        i+=1
                
    return target
    
    
#the annoying part of bitonic sort is that
#some parts of the sequence are sorted by descending order
#other parts of the sequence are sorted by ascending order
#for each primary iteration, we create a sorting order sequence for each element
#for each secondary iteration inside a primary iteration
#the sorting order for each element is the same
def get_direction(iteration_number,length):
    
    temp=iteration_number
    
    direction=[0]*length
    
    ind=[i for i in range(0,length,temp)]
    
    for i in ind[0::2]:
        direction[i]=1
    for i in ind[1::2]:
        direction[i]=-1
    
    for i in range(len(direction)):
        if direction[i]==0:
            direction[i]=direction[i-1]
            
    return direction
    


# In[3]:


for j in range(100):
    
    #bitonic sort only works on a list with 2**n elements
    target=[rd.randint(0,100) for i in range(2**rd.randint(0,10))]
    if bitonic_sort(target)!=sorted(target):
        print('Erreur')


