
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
# for i in range(0, 40, 5):
#     print(i)

""" LISTS - This is a list function where we have a list and
we double each value and return a doubled list
We can also unpack a list by putting variables in front of the = sign. NB You need to have
the same number of variables as are in the list"""
# simple_list = [1, 2, 3, 4]
# doubled_list =[]
# for element in simple_list:
#     doubled_list.append(element * 2)
# print(doubled_list)

# a, b, c, d = simple_list
# print(simple_list)
# print("This will print each element individually", a, b, c, d)
# print("This will print each element individually", a, d)


""" This is a list comprehension where we do the same as
above but all in one line without the need for a for loop """
# simple_list = [1, 2, 3, 4]
# doubled_list = [el * 2 for el in simple_list]
# print(doubled_list)


""" This is a list comprehension where we do the same as above but
include an if statement so only number divisible by 2 are returned """
# simple_list = [1,2,3,4]
# dup_list = [el * 2 for el in simple_list if el % 2 == 0]
# print(dup_list)


""" We have a stats list with key value pairs (tuples) and we convert them into a Dict
comprehension in dict_stats. This give us a dictionary"""
# stats = [("age", 29), ("weight", 72), ("height", 178)]
# print(stats)

# dict_stats = {key: value for (key, value) in stats}
# print(dict_stats)



""" The list example below shows that it is the REFERENCE not the VALUE that is copied over
from my_list to second_list. We changed the first element of second_list to hello! but it also
changed in my_list. """
# my_list = [1,2,3,4,5]
# second_list = my_list
# print("Secondlists first value:", second_list[0])
# second_list[0] = "hello!"
# print("Second list:", second_list)
# print("My list:", my_list)

""" Now, by using a 'range selector' [:] we actually copy the list, which gives us a NEW LIST
as in the example below. We add the range selector after my_list which allows us to copy it and
change elements in the copied list but keep the original"""
# my_list = [1,2,3,4,5]
# second_list = my_list[:]
# print("Secondlists first value:", second_list[0])
# second_list[0] = "hello!"
# print("Second list:", second_list)
# print("My list:", my_list)


""" Another way is to use the range selector is to define the new list as below. [0:3] takes
the first 3 elements from the list [0,1,2] as it is up to 3, not including. [:-2] excludes the
2 right most elements """
# simple_list = [6,7,8,9,10]
# new_list = simple_list[0:3]
# print("Simple list", simple_list)
# print("New list", new_list)
# new_list = simple_list[:-2]
# print("Simple list", simple_list)
# print("New list", new_list)
# new_list[1] = "Hello!"
# print("Simple list", simple_list)
# print("New list", new_list)

""" The range selector also works with tuples but NOT SETS or DICTIONARIES as sets and
dictionaries are not ordered """
# tuple = (1,2,3,4)
# print(tuple)
# print(tuple[0:2])
# print(tuple[:-1])
# print("This works for tuples")
# set = {"Alan", "Rachel", "Katrina", "Helen"}
# print(set[0])
# print(set[0:2])

""" Although we get no errors when coping the dictionary, the name is also changed in the stats
dictionary. This is because the range selector only copies a SHALLOW copy. This allowed us to
copy the list BUT NOT the nested data in memory"""
# stats = [{"name": "Alan"}, {"Age": 45}]
# print("Stats",stats)
# copied_stats = stats[:]
# print("Copied stats", copied_stats)
# copied_stats[0]["name"] = "Rachel"
# print("Stats",stats)
# print("Copied stats", copied_stats)


""" Comparing 'is' & '=='. As in the example below == compare the 2 lists and returns True.
'is' compares the 2 objects in memory and returns False"""
# simple_list = [1,2,3,4]
# second_list = [1,2,3,4]
# print(simple_list == second_list)
# print(simple_list is second_list)


""" DATA STRUCTURES for list. When we use '.' we get a list of what we can append"""
# simple_list = [1,2,3,4]
# print("Simple list", simple_list)
# simple_list.extend([5,6,7,8])
# print("Simple list extended", simple_list)
# del simple_list[1]
# print("Delete 2 from list", simple_list)


""" and for Dictionaires"""
# d = {"name": "Alan", "age": 45}
# print(d.items())
""" The .items returns a list of the dict_items as a tuple which allows us to get access to the
keys and values which can be used in a for loop"""
# for k, v in d.items():
#     print("Key and Value:", k, "&", v)
# del d["name"]
# print("Deleting name deletes the dictionary as there is no key to pair the value to", d)

""" LIST COMPREHENSION """
# print("List Comprehension with just Keys:", [el for el in d])
# print("List Comprehension with Keys & Values:", [el for el in d.items()])
# print("List Comprehension with just Values:", [el for el in d.values()])

""" FOR LOOP """
# for el in d:
#     print("For Loop with just Keys:", el)
# for el in d.items():
#     print("For Loop with Keys & Values:", el)
# for el in d.values():
#     print("For Loop just Values:", el)


""" and for Tuples we get less options with '.' If we try to delete from a Tuple we get an error
as Tuples are immutable"""
# t = (1,2,3)
# print("Returns the index of element 1:", t.index(1))


""" and for Sets, if we have the same element twice the first will be removed when returned.
If we use the delete function with set we also get an error.
To delete from a set use 'discard'"""
# s = {"Alan", "Rachel", "Katrina", "Helen", "Alan"}
# print(s)



""" ALL & ANY.  """
new_list = [True, True, False]
# print(new_list)
# print("'Any' checks if any of the values are True in the list:", any(new_list))
""" Any returns True (in this case) as it checks if the list holds at least 1 True value. """
# print("'All' checks if all of the values are True in the list:", all(new_list))
""" All returns False as it checks if all values in the list are True"""
# number_list = [1,2,3,4,-5]
# print(number_list)
""" 'number_list > 0' will error as > is not supported in this instance. We need to use
list comprehension to work out what elements are greater than 0"""
# print("This shows what elements are greater than 0:", [el for el in number_list if el > 0])

""" If we want to know if all elements are greater than 0 we use list comprehension with All"""
# print("This tells us if all elements are greater than 0, True or False:", all([el > 0 for el in number_list]))


""" FORMAT METHODS"""
# name = "Alan"
# age = 45
# print("I am " + name + " and I am " + str(age) + " years old.")

""" So rather than opening and closing brackets all the time we can use {} as placeholders in the one
string and add .format() after the string which will inject the values into the string. The order is
very important and obviously the number of placeholders needs to equal the number of arguments. This
can be changed by inputting numbers between the {}. e.g. {1} {0} would swap the name and age.
The 4th print is a new way of doing this but only on Python 3.6 or above. Print(f"")"""
# print("I am {} and I am {} years old.".format(name, age))
# print("I am {1} and I am {0} years old.".format(name, age))
# print("I am {0} and I am {1} years old. Yes I am really called {0}".format(name, age))
# print(f"I am {name} and I am {age:.2f} years old!")

""" {:.1f} tells the program that we want to return the value as a float with 1 decimal place."""
# funds = 150.9723
# print("Funds: {}".format(funds))
# print("Funds: {:.1f}".format(funds))



""" MAP FUNCTION
Without the list function we just get a <map object at ....> back so we use the list function in
front of the map function"""
simple_list = [1,2,3,4]

def multiply(el):
    return el * 2


# print("Returns a map object:", map(multiply, simple_list))
print("This runs our multiply function on our simple_list and returns the output:", list(map(multiply, simple_list)))
# print("This converts our simple_list into strings:", list(map(str, simple_list)))

""" LAMBDA FUNCTION """
# print("This uses a Lambda function which removes the need for the multiply function:", list(map(lambda el: el * 2, simple_list)))



""" UNPACKING FUNCTION ARGUMENTS with * """
def unlimited_arguments(*args):
    print("With (*args) we get a tuple which we can use inside the function:", args)
    for argument in args:
        print(argument)

unlimited_arguments(1,2,3,4)

a= [1,2,3,4,5]
print("Some text: {} {} {}".format(*a))

def dict_arguments(*args, **keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)

dict_arguments(name="Alan", age=45, hobbies=["electronics", "programming", "arduino"])
