from art import logo
print(logo)
print("\nWelcome to the Blind Auction!")

bidders = {}  # Stores each bidder's name and bid amount
continue_bidding = True

while continue_bidding:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount in dollars: $"))
    bidders[name] = bid  # Add bidder's information

    more_bidders = input("Is there anyone else who would like to bid? Type 'yes' or 'no': \n").lower()
    print("\n" * 200)  # Clear screen for confidentiality

    if more_bidders == "no":
        continue_bidding = False

# Find the highest bid and bidder
highest_bid = 0
highest_bidder = ""

for bidder_name in bidders:
    if bidders[bidder_name] > highest_bid:
        highest_bidder = bidder_name
        highest_bid = bidders[bidder_name]

print(f"\nThe highest bidder and winner is {highest_bidder} with a bid of ${highest_bid}.")
