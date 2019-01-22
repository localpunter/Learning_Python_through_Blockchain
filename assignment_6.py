# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.

# expecting_input = True
# while expecting_input:
#     print("Please choose: ")
#     print("1: Add your input")
#     print("q: Quit")
#     user_input = input("Your choice: ")
#     if user_input == "1":
#         store_data = input("Your inputted data is: ")
#         with open("assignment_6.txt", mode="a") as f:
#             f.write(store_data)
#             f.write("\n")
#     elif user_input == "q":
#         expecting_input = False


# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.

# expecting_input = True
# while expecting_input:
#     print("Please choose: ")
#     print("1: Add your input")
#     print("2: Output data")
#     print("q: Quit")
#     user_input = input("Your choice: ")
#     if user_input == "1":
#         store_data = input("Your inputted data is: ")
#         with open("assignment_6.txt", mode="a") as f:
#             f.write(store_data)
#             f.write("\n")
#     elif user_input == "2":
#         with open("assignment_6.txt", mode="r") as f:
#             file_content = f.readlines()
#             for line in file_content:
#                 print(line)
#     elif user_input == "q":
#         expecting_input = False

# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

# 4) Adjust the logic to load the file content to work with pickled/ json data.


import pickle
import json

expecting_input = True
user_input_list = []


while expecting_input:
    print("\nPlease choose from the list below: \n")
    print("1: Add your input")
    print("2: Output data")
    print("q: Quit")
    user_input = input("\nYour choice: ")
    if user_input == "1":
        store_data = input("Please input some data: ")
        user_input_list.append(store_data)
        with open("assignment_6.p", mode="wb") as f:
            f.write(pickle.dumps(user_input_list))
        # with open("assignment_6.txt", mode="w") as f:
        #     f.write(json.dumps(user_input_list))
    elif user_input == "2":
        with open("assignment_6.p", mode="rb") as f:
            file_content = pickle.loads(f.read())
        # with open("assignment_6.txt", mode="r") as f:
        #     file_content = json.loads(f.read())
            for line in file_content:
                print("\n",line)
    elif user_input == "q":
        expecting_input = False
    else:
        print("The value",user_input,"invalid! Please pick a value from the list.")
else:
    print("You have successfully quit!")


