from art import logo
from os import system, name

def clear_screen():
    if name == 'nt':
        system("cls")
    else:
        system("clear")

is_bidding_active = True
bidder_details = {}

while is_bidding_active:
    clear_screen()
    print(logo)
    bidder_name = input("What is your name?: ")
    bidder_price = float(input("What is your price?: $"))
    bidder_details[bidder_name] = bidder_price

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    is_bidding_active = False if more_bidders == 'no' else True

highest_bid = 0
winner = None

for key, value in bidder_details.items():
    if value > highest_bid:
        highest_bid = value
        winner = key

clear_screen()

print(f"The winner is {winner} with a bid of ${highest_bid}.")