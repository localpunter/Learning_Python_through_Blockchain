names = ["Alan", "Rachel", "Liam", "Claire", "Laura", "Connor", "Scott", "Ruth", "Alison", "Aaron", "Charlie", "Rudi", "Norman"]

print("All names and length")
print("--------------------")

for name in names:
    print(name, "has", len(name), "characters")


print("")

print("Names >5 characters")
print("-------------------")


for name in names:
    if len(name) > 5:
        print(name, "has", len(name), "characters")


print("")

print("Names with 'N' or 'n'")
print("---------------------")


for name in names:
    if ("n" or "N") in name:
        print(name)


print("")

print("Names with >5 characters and 'N' or 'n'")
print("---------------------------------------")


for name in names:
    if len(name) > 5 and ("n" or "N") in name:
        print(name)





print("")

print("Remove all names from list with 'while' loop")
print("--------------------------------------------")


while len(names) >= 1:
    names.pop()
    print(names)






