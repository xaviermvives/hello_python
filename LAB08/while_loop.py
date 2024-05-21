# create a Python script that asks the user to correctly guess a number.

# importing random library to generate random numbers
import random

number = random.randint(1,10) # random number between 1 and 10
isGuessRight = False # initialiting to False

print("Welcome to the Guess Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# by default we enter the loop
# it keeps looping until the user guesses the random number
while isGuessRight == False:
    guess = input("Guess a number between 1 and 10:")
    # if the guess is ok, we print a message & exit the loop
    if int(guess) == number: # input() gets strings by default, we need to convert it into integer
        print(f'Your guess: {guess} is equal to {number}. You win!')
        isGuessRight = True # we exit the loop 
    # if the guess is wrong, we print a message & continue the loop
    else:
        print(f'You guessed {guess}. Sorry, that is not it. Try again.')

