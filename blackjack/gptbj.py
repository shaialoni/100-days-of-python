import random

# Initialize the deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Initialize the player's and dealer's hands
player_hand = []
dealer_hand = []

# Initialize the player's and dealer's scores
player_score = 0
dealer_score = 0

# Draw the initial cards for the player and dealer
player_hand.append(random.choice(cards))
player_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))

# Determine the player's and dealer's scores
for card in player_hand:
    if card == 11 and player_score + card > 21:
        player_score += 1
    else:
        player_score += card
        
for card in dealer_hand:
    if card == 11 and dealer_score + card > 21:
        dealer_score += 1
    else:
        dealer_score += card
        
# Print the initial hands and scores
print("Player's hand: ", player_hand)
print("Player's score: ", player_score)
print("Dealer's hand: ", dealer_hand[0], "???")

# Player's turn
while True:
    choice = input("Do you want to hit or stand? (h/s) ")
    if choice.lower() == "h":
        new_card = random.choice(cards)
        player_hand.append(new_card)
        if new_card == 11 and player_score + new_card > 21:
            player_score += 1
        else:
            player_score += new_card
        print("Player's hand: ", player_hand)
        print("Player's score: ", player_score)
        if player_score > 21:
            print("Player busts! Dealer wins.")
            break
    elif choice.lower() == "s":
        break
    else:
        print("Invalid choice. Please enter 'h' or 's'.")

# Dealer's turn
while dealer_score < 17:
    new_card = random.choice(cards)
    dealer_hand.append(new_card)
    if new_card == 11 and dealer_score + new_card > 21:
        dealer_score += 1
    else:
        dealer_score += new_card
    print("Dealer's hand: ", dealer_hand)
    print("Dealer's score: ", dealer_score)
    if dealer_score > 21:
        print("Dealer busts! Player wins.")
        break

# Determine the winner
if player_score <= 21 and (dealer_score > 21 or player_score > dealer_score):
    print("Player wins!")
elif dealer_score <= 21 and (player_score > 21 or dealer_score > player_score):
    print("Dealer wins!")
else:
    print("It's a tie!")
