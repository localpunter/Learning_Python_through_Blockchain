name = input('what is your name? ')

age = int(input('what is your age? '))

def print_user_data():
    print(name, age)

#def print_values(arg1, arg2):
    #print(arg1, arg2) 

def print_decades_i_lived():
    return int(age / 10) 

print_user_data()
#print_values(45, 'abc')
print(print_decades_i_lived())
