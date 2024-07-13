#name=input("plz enter your name")
#message=""" welcome to the flight please shoe your tickets to air hostess they,ll take u to ur cabin"""
#print(message)
#ticketprice=int(input("enter the price of ticket"))
#if ticketprice <= 5000:
    
    #print("sir you have to travel in economy class ")

#elif ticketprice >= 5000 and ticketprice<=15000:
    #print("you have to travel in premium economy")
#elif ticketprice >=15000 and ticketprice<=20000:
    #print("sir u have to travel in business class")
#else:
    #print("you have to travel in first class")
    
    
    #loan situation
#name=input("plz enter the name of customer ")
#print("WELCOME",name)
#message="""" welcome to our bank 
#type1>>> for check balance
#type2>>> for deposit
#type3>>> for loan situation
#"""
#print(message)
#available_amount=int(input("plz enter the available amount"))
#task=int(input("plz enter your option:"))

#if task >=1 and task <=3:
    #print("welcome to our bank")
    #if task == 1:
        #print("your available amount is ",available_amount)
    #elif task==2:
        #deposit_amount=int(input("you can deposit your money"))
        #available_amount+=deposit_amount
        #print("your available_amount is",available_amount)
    #else:
        #withdrawal_amount=int(input("plz enter the amount of withdrawl"))
       # if withdrawal_amount < available_amount:
            #available_amount-=withdrawal_amount
            #print("your available_amount is",available_amount)
                 
            
        #elif withdrawal_amount > available_amount:
            # permission= input("if u want loan from bank type yes or no")
             
             #if permission == "yes":
                # loan = withdrawal_amount-available_amount
                # available_amount=0
                 #print("you van get loan from bank",loan)
                 #print("available_amount value",available_amount)
                 
            # else:
                # print("you said no so we cant give u loan")
              #
        
        #else :
           # print("person dont want to withdraw")
            
             
#else:
    #print("type inbetween 1to 5")
                
                
                
#name=input("plz enter the name of customer ")
#print("WELCOME",name)
message="""" welcome to our bank 
type1>>> for check balance
type2>>> for deposit
type3>>> for loan situation
"""
#print(message)
#available_amount=int(input("plz enter the available amount"))
#task=int(input("plz enter your option:"))
#if task >=1 and task <=3:
    #print("welcome to our bank")
    #if task == 1:
        #print("your available amount is ",available_amount)
    #elif task==2:
        #deposit_amount=int(input("you can deposit your money"))
       # available_amount+=deposit_amount
   #     #print("your available_amount is",available_amount)
    #else:
       # withdrawal_amount=int(input("plz enter the amount of withdrawl"))
        #if withdrawal_amount < available_amount:
            #available_amount-=withdrawal_amount
            #print("your available_amount is",available_amount)
                 
            
        #elif withdrawal_amount > available_amount:
             #permission= input("if u want loan from bank type yes or no")
             
             #if permission == "yes":
                 #loan = withdrawal_amount-available_amount
                 #available_amount=0
                # print("you van get loan from bank",loan)
                 #print("available_amount value",available_amount)
                 #loan_method=input("you can get loan plz specify method of paying it back monthly emi ,cash")
                 
                    #if loan_method=="emi":
                     #interest_rate=0.5
                     #loan=loan+(interest_rate*loan)
                     #print("you have to pay interest rate on emi ",loan)
                     
                 #else:
                    # print("you have to pay the cash equal to loan amount",loan)
                 
             #else:
                 #print("you said no so we cant give u loan")
              
        
        #else :
             #print("person dont want to withdraw")
            
             
#else:
   # print("type inbetween 1to 5")
                
                
                
                
name=input("plz enter the name of customer ")
print("WELCOME",name)
message="""" welcome to our bank 
type1>>> for check balance
type2>>> for deposit
type3>>> for loan situation
"""
print(message)
available_amount=int(input("plz enter the available amount"))
for i in range(0,10):
    
   task=int(input("plz enter your option:"))
   if task >=1 and task <=3:
       print("welcome to our bank")
       if task == 1:
          print("your available amount is ",available_amount)
       elif task==2:
           for j in range(0,10):
              deposit_amount=int(input("you can deposit your money"))
              available_amount+=deposit_amount
              print("your available_amount is",available_amount)
       else:
            for k in range(0,10):
               withdrawal_amount=int(input("plz enter the amount of withdrawl"))
               if withdrawal_amount < available_amount:
                  available_amount-=withdrawal_amount
                  print("your available_amount is",available_amount)
                 
            
               elif withdrawal_amount > available_amount:
                    permission= input("if u want loan from bank type yes or no")
             
                    if permission == "yes":
                      loan = withdrawal_amount-available_amount
                      available_amount=0
                      print("you van get loan from bank",loan)
                      print("available_amount value",available_amount)
                      loan_method=input("you can get loan plz specify method of paying it back monthly emi ,cash")
                 
                      if loan_method=="emi":
                        interest_rate=0.5
                        loan=loan+(interest_rate*loan)
                        print("you have to pay interest rate on emi ",loan)
                     
                      else:
                          print("you have to pay the cash equal to loan amount",loan)
                 
                    else:
                        print("you said no so we cant give u loan")
              
        
               else :
                   print("person dont want to withdraw")
            
             
else:
    print("type inbetween 1to 5")
                
                
                
                