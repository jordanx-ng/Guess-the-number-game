# Guess the number minigame

import random

print("Welcome to the Guess the Number Game!")
print("Can you guess the number I'm thinking of between 1 and 100?")
number_im_thinking_of = random.randint(1,100)
attempts = 0

while True:
    n = int(input("Please key in your guess: "))
    attempts +=1

    if n < number_im_thinking_of:
        print("Too low! Try again!")
    elif n > number_im_thinking_of:
        print("Too high! Try again!")
    else:
        print(f"Congratulations! You've guessed the number {number_im_thinking_of} in {attempts} attempts.")
        break







    