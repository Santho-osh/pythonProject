import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

def slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for a in range[cols]:
        column = []
        current_symbols = all_symbols[:]
        for b in range[rows]:
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(cols):



def deposit():
    while True:
        amount = input('How much would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than zero.')
        else:
            print('Please enter a number.')
    return amount


def line():
    while True:
        lines = input('Enter the number of lines to bet on (1 - ' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter valid number of lines.')
        else:
            print('Please enter a number.')
    return lines


def bet():
    while True:
        bets = input('What would you like to bet on each line? $')
        if bets.isdigit():
            bets = int(bets)
            if MIN_BET <= bets <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Please enter a number.')
    return bets


def main():
    balance = deposit()
    lines = line()

    while True:
        bets = bet()
        total_bet = bets * lines

        if total_bet > balance:
            print(f'You do not have enough balance to bet that amount. Your current balance is ${balance}')
        else:
            break

    print(f'You are betting ${bets} on {lines} lines. Total bet is equal to: ${total_bet}')
    print(balance, lines)


main()
