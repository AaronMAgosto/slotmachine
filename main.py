
def deposit():
    while True:
        amount = input("What Would you like to dposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Amount must be greater than 0.")
        else:
            print("Please return a number")          

    return amount