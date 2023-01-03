import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
os.system('clear')
print(logo)
bids = {}

def highest_bid(bid_amounts):
    winning_name = ""
    winning_bid = 0
    for bid in bid_amounts:
        if bid_amounts[bid] > winning_bid:
            winning_bid = bid_amounts[bid]
            winning_name = bid
            
    print(f"The winner is {winning_name} with a bid of ${winning_bid}")

def get_bid(bidder_name, bid_amount):
    bids[bidder_name] = bid_amount

keep_going = True

while keep_going:
    
    bid_name = input("Hello, please enter your name: ")
    bid_price = int(input("Please enter your bid amount: $"))
    bids[bid_name] = bid_price
    another_bidder = input("Is there another bidder? Please enter N to end collecting bids, or anything else to continue: ").lower()
    os.system('clear')
    if another_bidder == "n":
        keep_going = False

highest_bid(bids)