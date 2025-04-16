#define the menu of the restraunt

menu={
    "pizza": 319,
    "pasta": 230,
    "fries": 120,
    "coffee": 100,
    "chocolate shake":120
}

print("menu: ", menu)


#greet
print(f"Welcome to Hotel-del-luna")
print(f"Pizza: Rs319\nPasta: Rs230\nFries: Rs120\nCoffee:Rs100\nChocolate Shake: Rs120")


order_total =0 
#319+100=419

item_1 =input("Enter the name of item you want to order= ").lower()
if item_1 in menu:
      order_total += menu[item_1]
      print("Your item '{item_1}' has been added to your order.")
else:
      print("Please order something from the menu.")

#check if they want to order more
another_order = input("Do you want something else?  (Yes/No): " ).strip().lower()
if another_order == "yes":
    item_2 = input ("Enter the name of second item= ").lower()
    if item_2 in menu:
          order_total += menu[item_2]
          print(f"Item {item_2} has been added to the order")
    else:
          print(f"Ordered item '{item_2}' is not available!")
print(f"The Total amount of items is{order_total}")
          