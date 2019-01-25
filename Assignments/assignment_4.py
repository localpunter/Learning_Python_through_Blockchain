# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.

num_list = [1,2,3,4,5]

def square(args):
    return args ** 2

print("This is a function that accepts another as an arg and squares num_list:", list(map(square, num_list)))




# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.

print("This uses a Lambda function and multiplies num_list by 10:", list(map(lambda el: el * 10, num_list)))

# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.

print("My number list: {} {} {} {} {}".format(*num_list))

# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.

print("Number 1 from num_list centered in a 20 char column: '{:^20.1f}'".format(*num_list))