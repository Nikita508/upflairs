#  min
ls=[12,34,45,56,78]

def mymin(ls):
    i=12
    min=i
    for i in ls:
        if i<min:
            min=i
    return min
mymin(ls)
print(mymin(ls))
               
               
ls=[12,34,45,56,78]

def mymax(ls):
    i=12
    max=i
    for i in ls:# max
        if i>max:
            max=i
    return max
mymax(ls)
print(mymax(ls))



#sorting ascending order

#ls=[12,9,8,34,24,15,3]
def mysort(ls):
    #n=len(ls)
    
    for i in range(len(ls)):
        #for j in range(n-i-1):  # bubble sort
         for j in range(len(ls)-i-1):
        
        
           if ls[j] >ls[j+1]  :
               ls[j+1],ls[j]=ls[j],ls[j+1]  # bubble sort
    return ls
            
            
            
            
            
ls=[12,9,8,34,24,15,3]  
mysort(ls)
print(mysort(ls))           
            

# selection sort

def mysort1(ls):
    min=ls[0]
    for i in range(len(ls)):  ## selection sort
        for j in range (len(ls)):
            if min>ls[i]:
                min,ls[i]=ls[i],min
    return ls
ls=[12,45,43,32,56,21]
mysort1(ls)
print(mysort(ls))
            
            
            
            # insertion sorting
def mysort2(ls):
    for i in range(1,len(ls)):
        j=i-1
        key=ls[i]
        while(j>=0 and ls[j]>key):
            
             ls[j+1]=ls[j]
             j=j-1
        ls[j+1]=key
    return ls
ls=[12,3,45,43,32,21]
mysort2(ls)
print(mysort2(ls))