import random

words=['apple','bicycle','football,','television','car','gold','ball', 'tomato' ]


#randomly choose a word from the list
chosen_word = random.choice(words)
word_display=['_' for _ in chosen_word]  #create  alist of underscores
attempts=5 #number of allowed attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display: 
    print("\n" + " ".join(word_display))
    guess = input ("Guess a letter: ".lower()).strip()
    if guess in chosen_word:
         for index, letter in enumerate(chosen_word):
              if letter == guess:
                    word_display[index] = guess #reveal letter
    else:
         print("That letter doesn't appear in the word , silly!!!!.")
         attempts -= 1

         #game conclusion
         if '_' not in word_display:
              print("yayyyyy........ you guessed the word right !!!")
              print("". join(word_display))
              print("you won the game")
         else:
              print("you lost the game")
              print("The word was: " + chosen_word)
              print("Better luck next time!")