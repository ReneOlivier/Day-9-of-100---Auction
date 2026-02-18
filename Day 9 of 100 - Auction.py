# Day 9 of 100 - Auction Program


print("Welcome to the secret bidding war!")

user_inputs = {} # need blank dictionary to store user inputs

user_name = input("What is your name?: ")
user_bid = int(input("What is your bid?: $"))

user_inputs[user_name] = user_bid # add the user input to the dictionary

more_bids = input("Are there any other bidders? Type 'yes' or 'no': ")

while more_bids == 'yes':
    print("\n" * 35) # clear the screen by printing new lines
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))

    user_inputs[user_name] = user_bid # add the user input to the dictionary

    more_bids = input("Are there any other bidders? Type 'yes' or 'no': ")

winner = max(user_inputs, key=user_inputs.get)  # type: ignore # find the key with the highest value in the dictionary

print(f"The winner is {winner} with a bid of ${user_inputs[winner]}")



