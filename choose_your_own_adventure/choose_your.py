name=input ("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right.Which way would you like to go? ").lower()


if    answer == "left":
         answer == input ("You come to a river,you can walk around it or swim across ? Type walk to walk around and swim to swim across: ")

         if answer == "swim":
            print("You swam across and were eaten by an alligator. ")
         elif answer == "walk":
              print("You walked for many miles, and ran out of water and you the game.")
         else: 
              print("Not a valid option.You lose.")

elif  answer == "right":
      answer = input("You come to a bridge. Do you want to 'cross' it or go 'back'? ").lower()


      if answer == "back":
           print("You go climb a tree and look for next path.")

      elif answer == "cross":
           print("YOu return to the start")

      else:
          print("Not a valid option.You lose.")

else:
      print("Not a valid option.You lose.")

print("Thank you for trying", name)