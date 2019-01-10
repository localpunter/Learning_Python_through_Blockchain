# name = input('what is your name? ')

# age = int(input('what is your age? '))

# def print_user_data():
#     print(name, age)

# #def print_values(arg1, arg2):
#     #print(arg1, arg2)

# def print_decades_i_lived():
#     return int(age / 10)

# print_user_data()
# #print_values(45, 'abc')
# print(print_decades_i_lived())


# name = "Alan"
# age = 45

# if name == "Rachel" and age > 40 or age < 40:
#     print("Yes")

# if name == "Rachel" and (age > 30 or age < 40):
#     print("Hi Rachel!")
# else:
#     print("You're not Rachel!")

""" with 1 argument we print out from 0 up to the number argument(5)
i.e. 0,1,2,3,4 in this case """
# for i in range(5):
#     print(i)

""" with 2 arguments we print out from the first argument(5) up to the second argument(10)
i.e. 5,6,7,8,9 in this case """
# for i in range(5, 10):
#     print(i)

""" with 3 arguments we print out from the first argument(0) up to the second argument(40)
in increments of the third argument(5) i.e. 0,5,10,15,20,25,30,35 in this case
range ONLY WORKS with integers, + or - but NOT floats """
for i in range(0, 40, 5):
    print(i)



