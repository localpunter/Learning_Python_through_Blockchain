persons = {

    'name': ['Jonh', 'Julia', 'David', 'Ana', 'Carl'],

    'age': [31, 19, 21, 17, 27],

    'hobby': ['cooking', 'biking', 'Parkour', 'Creative writing', 'Singing']

}

names = [name for name in persons['name']]

print(names)

# ['Jonh', 'Julia', 'David', 'Ana', 'Carl']



older_than_twenty = ['%s: %s' % (name, age) for name, age in zip(persons['name'], persons['age']) if age > 20]

print(older_than_twenty)

# ['Jonh: 31', 'David: 21', 'Carl: 27']



names = persons['name'][:]

names[0] = 'Alex'

print(persons['name'])

print(names)



# ['Jonh', 'Julia', 'David', 'Ana', 'Carl']

# ['Alex', 'Julia', 'David', 'Ana', 'Carl']