# Exception handling
#try:
   # name=input("plz enter yr name")
    #age=int(input("plz enter yr age"))
   # print("i am",name, "and i am",age)
#exc#ept:
    #print("error is occurred but dont worry we'll execute your remaining code")
    
#else:
    #print("error is not occur")




#finally:
    #print("apple")
#print("i am important")

#a=int(input("enter something"))

#try:
    #num1=int(input("enter yr first number"))
    #num2=int(input("enter second number"))
    #res=num1/num2
    #print(res)
    #print("i am important")
#except ZeroDivisionError:
    #print("plz dont insert zero in second number")
    
    
#except ValueError:
    #print("plz enter a valid input or integer")
#print("i am important")
    
    
#print("hello') such errors are  undetectable


# quiz

ls=[52,41,63,96,745]
print(ls)

target=int(input("enter yr target item from list"))
position=int(input("plz enter a position"))
try:
    ls=[52,41,63,96,745]
    for i in range(len(ls)):
     if ls[i]==target:
        print (i)  # target
        

     for i in ls:
         if i==position:  #position
             print(ls[i])
except ValueError:
    print("there is error")
except IndexError:
    print("theres another error")



#  output the position of target value

# tell the value on position given by user



#try:
    #age=int(input('enter age'))
#except Exception as e:
    #print(e)
#except:
    #print('hii error occur')
    