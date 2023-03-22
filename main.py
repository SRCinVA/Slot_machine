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

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0 # initialize winnings to $0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] # we get the first element (0) of the line
        for column in columns:
            symbol_to_check = column[line] # we need to check each column at position "line" (whether index 1 or 2, checked against index 0)
            if symbol != symbol_to_check:
                break # if they're not equal, there's no need to continue, so you break out.
            else:
                winnings += values[symbol] * bet # the multiplier for that symbol * whatever bet they made. The bet is for a single line, which we can add to.
                winning_lines.append(lines + 1) # we add '1' to the index so we can report which line the user won.

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # the ".items" syntax gives you both the key and the value associated with a dictionary
        for _ in range(symbol_count):  # you can use an anonymous variable _ here, if you don't care about the name.
            all_symbols.append(symbol) # b/c of the embedded for loop, we'll be adding the items (numbers) twice.

    columns = []  # this will be a list of lists to make up the columns
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # this syntax *copies* the list all_symbols, and does not turn it into a reference. We need to take options away with each spin and retain the information that it has been removed.
        for _ in range(rows): # "rows" gives us the total number of rows we have in the slot machine
            value = random.choice(current_symbols)
            current_symbols.remove(value) # it finds the first instance of the value in the list and gets rid of it.
            column.append(value) # ... ten we add that value to the column[].
        
        columns.append(column) # last, we append that column to the columns list

    return columns

def print_slot_machine(columns): # we need to transpose the matrix in this function
    for row in range(len(columns[0])):  # the length of the row is determined by the length of a column. [0] assumes that there will always be one column.
        for i, column in enumerate (columns): # here, we will only print the index of the current row
            if i != len(columns) -1:
                print(column[row], end = " | ")  # above, we get the index AND the item itself as we loop through. 
            else:
                print(column[row], end = "")  # don't know why we would *not* have the pipe here.
                                                # 'end' is by defualt the \n or new line character, to make the print out horizontal
        print()  # basically, thsi will create an empty line

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

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # no explanation as to why these particular variables are passed in
    print(f"You won ${winnings}.")
    print(f"You won on", *winning_lines) # the "splat" or "unpack" operator

main()
