import random
import art
from game_data import data
import os

def compare(first, second):
    if first['follower_count'] > second['follower_count']:
        return first
    else:
        return second

def game():
#compare random a
    score = 0
    game_message = ""
    game_on = True
    compare_a = data[random.randint(0, 49)]
    
    while game_on:
        compare_b = data[random.randint(0, 49)]
        os.system('clear')
        print(art.logo)
        print(f"{game_message}")
        print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}. {compare_a['follower_count']}")
        print(art.vs)
        print(f"Against B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}.{compare_b['follower_count']}")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        print('answer from input', answer)
        if answer == 'a':
            answer = compare_a
            print('answer A', answer)
        elif answer == 'b':
            answer = compare_b
            print('answer B', answer)
        if answer == compare(compare_a, compare_b):
            score += 1
            game_message = f"You are correct! Current score {score}"
            compare_a = answer
        else:
            game_on = False
            os.system('clear')
            print(art.logo)
            print(f"You didn't get that last one... Your final score is {score}")

game()
#random B

#make a decision

#compare winner vs new random and so on.