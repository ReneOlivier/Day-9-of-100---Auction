# Secret Bidding Auction Program

## Overview
A command-line auction program where multiple bidders can submit their bids anonymously. The program collects bids from all participants and automatically determines the winner with the highest bid.

## Features
- **Multiple Bidders**: Accept bids from any number of participants
- **Anonymous Bidding**: Screen clears between entries to maintain bidder privacy
- **Automatic Winner Detection**: Finds and announces the highest bidder
- **User-Friendly Interface**: Clear prompts and welcoming messages

## How It Works
1. Welcome message displays
2. First bidder enters their name and bid amount
3. Program asks if there are more bidders
4. Screen clears (prints newlines) to hide previous bids
5. Additional bidders enter their information
6. Once all bids are collected, the program announces the winner with their bid amount

## How to Run
```bash
python "Day 9 of 100 - Auction.py"
```

## Example Output
```
Welcome to the secret bidding war!
What is your name?: Alice
What is your bid?: $100
Are there any other bidders? Type 'yes' or 'no': yes

[Screen clears...]

What is your name?: Bob
What is your bid?: $150
Are there any other bidders? Type 'yes' or 'no': no

The winner is Bob with a bid of $150
```

## Skills Learned
- **Dictionaries**: Storing and managing key-value pairs (bidder names and amounts)
- **User Input**: Collecting data from users with the `input()` function
- **Type Conversion**: Converting string input to integers with `int()`
- **Loops**: Using `while` loops to repeat bidding process
- **Built-in Functions**: Using `max()` with a `key` parameter to find the highest value
- **String Formatting**: Using f-strings to display formatted output
- **Screen Clearing**: Implementing simple privacy by clearing the console with newlines
- **Dictionary Methods**: Using `.get()` method for dictionary value access
- **Type Hints & Linting**: Suppressing type checker warnings with `# type: ignore`

## Code Concepts
| Concept | Example |
|---------|---------|
| Dictionary Creation | `user_inputs = {}` |
| Dictionary Assignment | `user_inputs[user_name] = user_bid` |
| Conditional Loop | `while more_bids == 'yes':` |
| Finding Maximum | `max(user_inputs, key=user_inputs.get)` |
| F-String Formatting | `f"The winner is {winner} with a bid of ${user_inputs[winner]}"` |
