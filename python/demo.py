MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Slots
def deposit():
    while True:
        amount = input("Enter amount to be deposited: E")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero...")
        else:
            print("Amount must be a number!")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines  = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid amount of lines...")
        else:
            print("Amount must be a number!")

    return lines

def get_bet():
    while True:
        amount = input("Enter amount to be bet on each line: E")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET} ...")
        else:
            print("Amount must be a number!")

    return amount    


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = lines * bet

    print(f"You are betting $(bet) on {lines} lines... Total bet: ${total_bet}...")



main()

