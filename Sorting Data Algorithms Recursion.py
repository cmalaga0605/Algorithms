#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Bubble Sort (not considered practical)
def bubbleSort(dataset):
    #TODO:Start with the array length and decrement each time
    for i in range(len(dataset)-1,0,-1): #start with the last item and then go untill the last item and go down by one
        for j in range (i):
            if dataset[j]>dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1]= temp 
        print("Current state: ", dataset)

def main():
    list1 = [6,20,8,19,56,23,87,41,49,53]
    bubbleSort(list1)
    print("Result: ", list1)
    
if __name__ == "__main__":
    main()


# In[ ]:


#Merge Sort Known as the divide and conquer algorithm log linear
#Break up an array to elements and than bring them back together sorted

items = [6,20,8,19,56,23,87,41,49,53]

def mergesort(dataset):
    if len(dataset)>1:
        mid = len(dataset)//2
        leftarr=dataset[:mid]
        rightarr=dataset[mid:]
        
        #TODO: recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)
        
        #TODO: now perform the merging
        i=0 #index into the left array
        j=0 #index into the rightarray 
        k=0 # index into merged array
        
        #TODO: while arrays have content
        while i <len(leftarr) and j<len(rightarr):
            if leftarr[i]<rightarr[j]:
                dataset[k]=leftarr[i]
                i+=1
            else:
                dataset[k]=rightarr[j]
                j+=1
            k+=1
        #TODO if the left array still has values,add them
        while i<len(leftarr):
            dataset[k] = leftarr[i]
            i +=1 
            k+=1
        
        #TODO: if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j+=1 
            k+=1
            
print(items) #unsorted
mergesort(items) #sorted
print(items) #sorted printed


# In[1]:


#quick sort algorithm
items = [20,6,8,53,56,23,87,41,49,19]

def quickSort(dataset,first,last):
    if first < last:
        #calculate the split point
        pivotIdx = partition(dataset,first,last)
        
        #now sort the two partitions
        quickSort(dataset,first,pivotIdx-1)
        quickSort(dataset,pivotIdx+1,last)

def partition(datavalues,first,last):
    #choose the first item as the pivot value
    pivotvalue = datavalues[first]
    #establish the upper and lower indexes
    lower = first + 1
    upper = last
    
    #start searching for the crossing point
    done = False
    while not done:
        #TODO: advance the lower index
        while lower <= upper and datavalues[lower] <=pivotvalue:
            lower +=1
        #TODO: advance the upper index
        while datavalues[upper] >= pivotvalue and upper >=lower:
            upper-=1
        #TODO: if the two indexes cross, we have found the split point
        if upper <lower:
            done = True
        else: 
            temp= datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp
  
    #When the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp
    
    #return the split point index 
    return upper

#test the merge sort with data
print(items)
quickSort(items,0,len(items)-1)
print(items)
    


# In[ ]:




