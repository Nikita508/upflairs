# dictionary for defining menu
menu={'pizza':400,'salad':120,'burger':40,'coffee':100,'fries':60}
# Greet
print("welcome to my cafe")
print("pizza:Rs400\nsalad:120\nburger:40\ncoffee:100\nfries:60")
total_order=0
item1=input("enter the item you want to order")
if item1 in menu:
    total_order+=menu[item1]
    print("yr item {item1} has been ordered")
else:
    print("ordered item {item1} is not available")
another_order=input("Do you want to order something else say(yes/no)")
if another_order=="yes":
    item2=input("enter second item name=")
    if item2 in menu:
        total_order+=menu[item2]
        print("yr item {item1} has been ordered")
    else:
        print("ordered item{item2}is not available")
print("total amount of item is {total_order}")
        
        
    