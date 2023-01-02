# This page is the source to different sorting algorithms 

def sort_bubble(a):  ##Bubble sort algorithm
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return(a)

def linear_search(a,n):   ##linear search algorithm
    for i in range(len(a)):
        if a[i]==n:
            return(i)
    return('False')
        
def max_value(a,b):     ##gives max value in lists
    if(a>b):
        max=a
    else:
        max=b
    return(max)

def max_list(a):
    max=a[0]
    for i in range(1,len(a)):
        if (a[i]>max):
            max=a[i]
    return(max)

#returns keys in nested dictionary
def rec_keys(dictio):
    keys = []
    for (key,value) in dictio.items():
        if isinstance(value,dict):
            keys.extend(rec_keys(value))
        else:
            keys.append(key) 
    return keys   

def rec_keys_2(dictio):
    keys = str(input)
    for (key,value) in dictio.items():
        if isinstance(value,dict):
            keys.extend(rec_keys_2(value))
        else:
            keys.append(key) 
    return keys 
        