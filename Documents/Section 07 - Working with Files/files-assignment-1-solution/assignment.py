# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
# running = True

# while running:
#     print('Please choose')
#     print('1: Add input')
#     print('2: Output data')
#     print('q: Quit')
#     user_input = input('Your Choice: ')
#     if user_input == '1':
#         data_to_store = input('Your text: ')
#         with open('assignment.txt', mode='a') as f:
#             f.write(data_to_store)
#             f.write('\n')
#     elif user_input == '2':
#         with open('assignment.txt', mode='r') as f:
#             file_content = f.readlines()
#             for line in file_content:
#                 print(line)
#     elif user_input == 'q':
#         running = False
# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.
import json
import pickle

running = True
user_input_list = []

while running:
    print('Please choose')
    print('1: Add input')
    print('2: Output data')
    print('q: Quit')
    user_input = input('Your Choice: ')
    if user_input == '1':
        data_to_store = input('Your text: ')
        user_input_list.append(data_to_store)
        with open('assignment.p', mode='wb') as f:
            # f.write(json.dumps(user_input_list))
            f.write(pickle.dumps(user_input_list))
    elif user_input == '2':
        with open('assignment.p', mode='rb') as f:
            file_content = pickle.loads(f.read())
            for line in file_content:
                print(line)
    elif user_input == 'q':
        running = False
# 4) Adjust the logic to load the file content to work with pickled/ json data.
