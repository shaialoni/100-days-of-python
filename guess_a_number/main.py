import random
from art import logo
#Guess the number game
print(logo)

# A user will start the game, welcome screen, computer guess number and offer difficulty level choice
print("Welcome to Guess The Number. I have picked a number between 1 and 100, care to guess it???")
picked_number = random.randint(1,100)
print(f"(Psst... I picked {picked_number})")

# User has to select the difficulty level
select_difficulty = input("Please select hard or easy difficulty 'h'/'e': ").lower()
if select_difficulty == 'h':
    number_of_attempts = 5
elif select_difficulty == 'e':
    number_of_attempts = 10
else:
    print("You did not enter a valid choice, goodbye.")

# Computer presents the number of attempts basded on the level picked
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

# User has to start guessing and get feedback from the computer after each guess.

# Game ends when user guesses correct number or number of attempts ran out.
