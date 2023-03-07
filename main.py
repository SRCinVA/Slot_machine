
from curses.ascii import isdigit


def deposit(): # this one will collect user input
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():  # needs to a positive whole number
            amount = int(amount) # need to cast it as an int
            if amount > 0:
                break
            else:
                print("your amount must be greater than 0.")
        else:
            print("Please enter a number.")
