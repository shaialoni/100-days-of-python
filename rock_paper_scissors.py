rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]
tie = "This is a TIE!"
win = "You WON!!!"
lost = "You lost :("

computer_choice = random.randint(0, 2)
player_choice = int(input("0 - Rock, 1 - Paper or 2 - Scissors? Please select 1, 2 or 3 \n"))
if player_choice >=3 or player_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f'''
    Computer chose: {game_images[computer_choice]}
    You chose: {game_images[player_choice]}
    ''')

if player_choice == 0 and computer_choice == 2:
    print(f"{win}")
elif computer_choice == 0 and player_choice == 2:
    print(f"{lost}")
elif computer_choice > player_choice:
    print(f"{lost}")
elif player_choice > computer_choice:
    print(f"{win}")
elif computer_choice == player_choice:
    print(f"{tie}")