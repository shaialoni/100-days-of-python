import random
from art import logo, vs
from game_data import data
import os


def clear_screen():
    os.system('clear')


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"


def compare(first, second):
    if first['follower_count'] > second['follower_count']:
        return first
    else:
        return second


def game():
    score = 0
    game_message = ""
    game_on = True
    compare_a = data[random.randint(0, 49)]

    while game_on:
        compare_b = data[random.randint(0, 49)]
        if compare_a == compare_b:
            compare_b = data[random.randint(0, 49)]

        clear_screen()
        print(logo)
        print(f"{game_message}")
        print(f"Compare A: {format_data(compare_a)}")
        print(vs)
        print(f"Against B: {format_data(compare_b)}")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        # print('answer from input', answer)
        if answer == 'a':
            answer = compare_a
            # print('answer A', answer)
        elif answer == 'b':
            answer = compare_b
            # print('answer B', answer)
        if answer == compare(compare_a, compare_b):
            score += 1
            game_message = f"You are correct! Current score {score}"
            compare_a = answer
        else:
            game_on = False
            clear_screen()
            print(logo)
            print(f"You didn't get that last one... Your final score is {score}")


game()
