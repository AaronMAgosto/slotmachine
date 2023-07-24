# We first import the 'random' module which allows us to make random choices
import random

# We define some constants that we will use throughout our code
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# This is a dictionary that shows how many of each symbol there are in the slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# This function simulates a spin of the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    # We first build a list of all symbols in the machine
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    # Then we build the slot machine itself as a list of columns, where each column is a random selection of symbols
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for column in columns:
            print(column[row], "")

# This function asks the user how much money they want to deposit into the slot machine
def deposit():
    while True:
        amount = input("What Would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Amount must be greater than 0.")
        else:
            print("Please return a number")          

    return amount

# This function asks the user how many lines they want to bet on
def get_number_of_lines():
    while True:
        lines = input(" Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("enter a valid number of lines")
        else:
            print("Please enter a number")          

    return lines

# This function asks the user how much they want to bet on each line
def get_bet():
    while True:
        amount = input("What Would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                print(f"Amount must be between. ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please return a number")          

    return amount

# This is the main function that ties everything together
def main():
    # First, the user deposits some money into the slot machine
    balance = deposit()
    # Then, they decide how many lines they want to bet on
    lines = get_number_of_lines()
    while True:
      # They decide how much to bet on each line
      bet = get_bet()
      # We calculate the total bet
      total_bet = bet * lines

      # If the total bet is more than the user's balance, we ask them to enter a smaller bet
      if total_bet > balance:
          print(
              f"you do not have enough to bet that amount, your current balance is: ${balance}")
      else:
          break    
    # Finally, we print out a summary of the user's bet
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")


# This line starts the whole process by calling the main function
main()
