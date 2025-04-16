print("Welcome to my computer quiz!")

playing=input("Do you want to play?(yes/no) ")


if playing.lower()  !="yes":
    quit()


print("OKay! Let's play  : )")
score=0

answer = input("Who's the president of the USA? ")
if answer.lower() == "donald trump":
   print("Correct!")
   score += 1
else:
    print("Incorrect!")


answer = input("Who's the best football player? ")
if answer.lower()  == "cristiano ronaldo":
   print("Correct!")
   score += 1
else:
    print("Incorrect!")


answer = input("What's the capital of Japan?")
if answer.lower()  == "tokyo":
   print("Correct!")
   score += 1
else:
    print("Incorrect!")

answer = input("What's the national game of England? ")
if answer.lower() == "cricket":
   print("Correct!")
   score += 1
else:
    print("Incorrect!")


answer = input("Which vitamin do you get from sunlight? ")
if answer.lower() == "vitamin d":
   print("Correct!")
   score += 1
else:
    print("Incorrect!")


answer = input ("Which country is known as the Land of the Rising Sun? ")
if answer.lower() == "japan":
   print("Correct!")
   score += 1
else:
    print("Incorrect!")

print("You got  "+ str(score)+ " questions correct!")
print("You got  "+ str(round((score / 6)* 100 , 2))+ "%")