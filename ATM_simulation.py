name =input("plz enter your name")
print("welcome",name)
message = """
how may i help u sir.
please select any of them option,
type1 >>>>check balance
type2>>>>deposit
type3>>>>withdrawl."""
print(message)
task=int(input("plz enter your option:"))
available_amount=5000
if task >=1 and task <=3:
    print("welcome to u in virtual bank")
    #check balance
    if task==1:
        print("your available amount is:",available_amount)
    #deposit
    elif task==2:
        deposit_amount=int(input('plz enter deposit amount:'))
        if deposit_amount >500:
            available_amount+=deposit_amount
            print("amount deposited successfully",deposit_amount)
            print("your available amount is:",available_amount)
        else:
            print("throw it")
    #withdrawl
    else:
        withdrawl_amount=int(input('plz enter withdrawl amount:'))
        if withdrawl_amount < available_amount:
            available_amount-=withdrawl_amount
            print("amount withdrawl successfully")
            print("your available amount is:",available_amount)
        else:
            print("paisa khatam")
            
            
            
else:
    print("plz select in between 1 to 5")