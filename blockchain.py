# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain.
    If no value exists it returns None """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction, last_transaction=[1]):
    """ Appends a new value as well as the last value to the blockchain """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount)
    as a float """
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        print(block)
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print('Please choose:')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print("Invalid blockchain")
        break

    print('Choice registered!')


print('Done!')
