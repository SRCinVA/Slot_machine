from curses.ascii import isdigit

MAX_LINES = 3  # this is a global constant, written in all caps by convention.
MAX_BET = 100
MIN_BET = 1

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
    bet = get_bet()
    print(balance, lines, bet)

main()