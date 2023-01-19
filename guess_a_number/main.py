#Guess the number game
# A user will start the game, welcome screen, computer guess number and offer difficulty level choice
# User has to select the difficulty level
# Computer presents the number of attempts basded on the level picked
# User has to start guessing and get feedback from the computer after each guess.
# Game ends when user guesses correct number or number of attempts ran out.

from random import randint
from art import logo

HARD_LEVEL = 5
EASY_LEVEL = 10
print(logo)

print("Welcome to Guess The Number. I have picked a number between 1 and 100, care to guess it???")
picked_number = randint(1,100)
print(f"(Psst... I picked {picked_number})")

def set_difficulty():
    select_difficulty = input("Please select hard or easy difficulty 'h'/'e': ").lower()
    if select_difficulty == 'h':
        return HARD_LEVEL
    elif select_difficulty == 'e':
        return EASY_LEVEL
    else:
        print("You did not enter a valid choice, goodbye.")

number_of_attempts = set_difficulty()

while number_of_attempts > 0:
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    user_guess = int(input("Please enter your guess: "))
    if  user_guess == picked_number:
        print(f"     You are correct!!! the answer was {picked_number}")
        break
    elif user_guess > picked_number:
        print("Hmm.. too high. ")
        if number_of_attempts > 1:
            print("Guess again!")
        else:
            print("You have ran out of guesses. You lose!")
    elif user_guess < picked_number:
        print("Hmm.. too low. ")
        if number_of_attempts > 1:
            print("Guess again!")
        else:
            print("You have ran out of guesses. You lose!")
    number_of_attempts -= 1




