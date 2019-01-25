# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.

""" Dictionaries use {} and lists use []. All persons have
their own dictionary and a list [] of hobbies. All persons
are then wrapped in a list"""
persons = [
    {
        "name": "Alan",
        "age": 45,
        "hobbies": ["Electronics", "Arduino", "Programming"],
    },
    {
        "name": "Rachel",
        "age": 37,
        "hobbies": ["Baking", "Walking", "Reading"],
    },
    {
        "name": "Morgan",
        "age": 43,
        "hobbies": ["Walking", "Tinkering", "Fishing"],
    }
]

""" Prints all dictionaries on 1 line"""
# print("This is my person dictionary:", persons)

""" Prints each persons dictionary on a separate line"""
for el in persons:
    print("This is", el ["name"], "'s dictionary:", el)


# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).

# print("List Comprehension with just Values:", [el for el in persons.values()])
# print("List Comprehension with Keys & Values:", [(el) for (k, el) in persons.items()])

names = [el ["name"] for el in persons]
print("List Comprehension with just names:", names)


# 3) Use a list comprehension to check whether all persons are older than 20.

all_ages_over_20 = all([el ["age"] > 20 for el in persons])
print("Are all ages over 20?", all_ages_over_20)



# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).

copied_names = names[:]
copied_names[0] = "Bawbag"
print("Copied names with the first name changed:", copied_names)
print("Original list of names unchanged:", names)


# 5) Unpack the persons of the original list into different variables and output these variables.

p_1, p_2, p_3 = persons
print("These are the original people unpacked as different vars:", p_1, p_2, p_3)
print("Person 2 only:", p_2)
