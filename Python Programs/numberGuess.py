#Garrett Gruber
#April 25, 2020
#A simple guessing game Python program to refresh my skills with the language.

import random
n = random.randint(1,100)
#print(n)
print("Guess a number between 1 and 100 (inclusively)")
guess = int(input("Your guess: "))
#print(guess)
if n == guess:
    print("Your guess is CORRECT.")
else:
    while n != guess:
        if guess < n:
            print("You guessed TOO LOW.")
            print("Guess another number between 1 and 100 (inclusively)")
            guess = int(input("Your guess: "))
        elif guess > n:
            print("You guessed TOO HIGH.")
            print("Guess another number between 1 and 100 (inclusively)")
            guess = int(input("Your guess: "))
    print("Your guess is CORRECT.")
    
