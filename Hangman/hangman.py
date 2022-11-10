import random
from hangman_art import stages, logo
from hangman_words import word_list
import os

end_game = False
chosen_word = random.choice(word_list)
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
print(logo)
display = []

for letter in chosen_word:
        display.append("_")

while not end_game:   
    guess = input("Guess a letter: ").lower()
    os.system('clear')

    if guess in display:
        print(f"You've already guessed {guess}")
        
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = guess
    print(f"{' '.join(display)}")        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("Game Over, you lose.")
            end_game = True
       
    if "_" not in display:
        end_game = True
       
        print("Congratulations, you won!")
        
    print(stages[lives])