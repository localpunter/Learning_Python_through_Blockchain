# 1) Create a list of names and use a for loop to output the length of each name (len()).
names = ['Max', 'Anna', 'Manuel', 'Chris', 'Stephen']

for name in names:
    print(name)
    print(len(name))
# 2) Add an if check inside the loop to only output names longer than 5 characters.
print('-' * 30)
for name in names:
    if len(name) > 5:
        print(name)
        print(len(name))
# 3) Add another if check to see whether a name includes a “n” or “N” character.
print('-' * 30)
for name in names:
    if len(name) > 5 and ('N' in name or 'n' in name):
        print(name)
        print(len(name))
# 4) Use a while loop to empty the list of names (via pop())
print('-' * 30)
while len(names) >= 1:
    print(names.pop())

print(names)
