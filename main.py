from curses.ascii import isdigit

MAX_LINES = 3  # this is a global constant, written in all caps by convention.

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
        lines = input("Enter the numebr of lines to bet on (1- " + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter 1, 2, or 3.")
            
    return lines

def main():
    balance = deposit()

main()
