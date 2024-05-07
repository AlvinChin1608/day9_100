import os
from art import logo

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

bids = {}
bidding_finished = False

while not bidding_finished:
  name = input("Please insert your name: ")
  price = int(input("What is your bid: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'y' or 'n': ")
  if should_continue == "n":
    bidding_finished = True
  elif should_continue == "y":
    clear_screen()
  else:
    print("Invalid input. Please type 'y' or 'n'.")

# Clear the screen
clear_screen()

# Display bid results
"""
print("Bidding has finished.")
highest_bid = max(bids.values())
highest_bidder = [name for name, bid in bids.items() if bid == highest_bid][0]
print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")
"""

# Display bid results
print("Bidding has finished.")
winner = max(bids, key=bids.get)
highest_bid = bids[winner]
print(f"The highest bidder is {winner} with a bid of ${highest_bid}.")