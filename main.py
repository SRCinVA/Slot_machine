from curses.ascii import isdigit
import random

MAX_LINES = 3  # this is a global constant, written in all caps by convention.
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D":8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items:
        pass

def deposit(): # this one will collect user input
    while True: # this is just going to continue to run until we break out of it.
        amount = input("What would you like to deposit? $")
        if amount.isdigit():  # needs to a positive whole number
            amount = int(amount) # need to cast it as an int
            if amount > 0:
                break # if they entered legit data, we can break out of the loop because we have the info we need.
            else:
                print("Your amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:  # this is just going to continue to run until we break out of it.
        lines = input("Enter the number of lines to bet on (1- " + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter 1, 2, or 3.")
            
    return lines

def get_bet():
        while True:
            amount = input("Enter the size of your bet (" + str(MIN_BET) + "-" + str(MAX_BET) + "): $")
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print(f"The amount must be between ${MIN_BET} - ${MAX_BET}.")
            else:
                print("Please enter an amount.")

        return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet >= balance:
            print(f"You don't have that much money; your current balance is ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. The total bet is equal to ${total_bet}.")

main()
