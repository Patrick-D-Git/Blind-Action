from replit import clear  # you will need to add the replit package if using IDE
from art import logo


def find_bid_winner(bidding_record):
    highest_bid = 0
    highest_bidder = ""

    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            highest_bidder = bidder

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


print(logo)
print("Welcome to the Secret Auction Program")

add_participants = True
bidding_participants = {}

while add_participants:

    participant_name = input("What is your name?: ")
    participant_bid = int(input("What's your bid?: $ "))
    bidding_participants[participant_name] = participant_bid

    if input("Are there any other bidders? Type 'yes' or 'no': ") == "no":
        add_participants = False

        find_bid_winner(bidding_participants)

    else:
        clear()
