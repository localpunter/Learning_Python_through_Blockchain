# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
def transform_data(fn):
    print(fn(10))
# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
transform_data(lambda data: data / 5)
# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed. 
def transform_data2(fn, *args):
    for arg in args:
        print(fn(arg))

transform_data2(lambda data: data / 5, 10, 15, 22, 30)
# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
def transform_data3(fn, *args):
    for arg in args:
        print('Result: {:^20.2f}'.format(fn(arg)))

transform_data3(lambda data: data / 5, 10, 15, 22, 30)