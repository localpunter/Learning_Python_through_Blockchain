# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
persons = [
    {
        'name': 'Max',
        'age': 29,
        'hobbies': ['Sports', 'Cooking']
    },
    {
        'name': 'Anna',
        'age': 28,
        'hobbies': ['Dancing']
    },
    {
        'name': 'Manu',
        'age': 33,
        'hobbies': ['Eating']
    }
]
# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
person_names = [person['name'] for person in persons]
print(persons)
print(person_names)
# 3) Use a list comprehension to check whether all persons are older than 20.
are_older = all([person['age'] > 20 for person in persons])
print(are_older)
# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
# copied_persons = persons[:]
copied_persons = [person.copy() for person in persons]
copied_persons[0]['name'] = 'Maximilian'
print(copied_persons)
print(persons)
# 5) Unpack the persons of the original list into different variables and output these variables.
p1, p2, p3 = persons
print(p1)
print(p2)
print(p3)
