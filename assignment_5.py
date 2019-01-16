import random
import datetime

# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.

ran_number = random.random()
print("This is a random number between 0 & 1:", ran_number)

new_ran_number = random.randint(1,10)
print("This is a random number between 1 & 10:", new_ran_number)



# 2) Use the datetime library together with the random number to generate a random, unique value.

now = datetime.datetime.now()
print (now, new_ran_number)
# print("This is an unique value generated by today's date & time and a random number 1 - 10:"(now, new_ran_number))

unique_value = (now, new_ran_number)
print("This isn't quite the unique value I thought I would get:", (unique_value))

# Added after solution
uv = str(new_ran_number) + str(now)
print("This is a new unique number:", uv)

