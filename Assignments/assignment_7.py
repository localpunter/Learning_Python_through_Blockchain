# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe()” method (which prints “name” and “kind” in a sentence).

class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    # Overwrite a “dunder” method to be able to print your “Food” class.
    def __repr__(self):
        return "Name: {}, Kind: {}".format(self.name, self.kind)

    def describe(self):
        print("\nTask 1: I like to eat a {} {}.\nIt is delicious!".format(self.kind, self.name))

    def eat1(self):
        print("\nI like {} with {} sauce".format(self.name, self.kind))

    def eat2(self):
        print("\n{} is my favourite {}".format(self.name, self.kind))

apple = Food("apple", "Granny Smith")
apple.describe()

pork = Food("pork", "chop")
pork.describe()




# 2) Try turning describe() from an instance method into a class and a static method. Change it back to an instance method thereafter.

# class Food:
#     name = ""
#     kind = ""

#     @classmethod
#     def describe(cls):
#         print("Task 2 '@classmethod': I like to eat a {} {}.\nIt is delicious!".format(cls.kind, cls.name))

# Food.name = "apple"
# Food.kind = "Granny Smith"
# Food.describe()


# class Food:

#     @staticmethod
#     def describe(name, kind):
#         print("Task 2 '@staticmethod': I like to eat a {} {}.\nIt is delicious!".format(kind, name))

# name = "Apple"
# kind = "Granny Smith"

# Food.describe(name, kind)


# class Food:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind

#     def describe(self):
#         print("\nTask 1: I like to eat a {} {}.\nIt is delicious!".format(self.kind, self.name))

#     def eat1(self):
#         print("\nI like {} with {} sauce".format(self.name, self.kind))

#     def eat2(self):
#         print("\n{} is my favourite {}".format(self.name, self.kind))

# apple = Food("apple", "Granny Smith")
# apple.describe()

# pork = Food("pork", "chop")
# pork.describe()

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook()” method to “Meat” and “clean()” to “Fruit”.
# 4) Overwrite a “dunder” method to be able to print your “Food” class.
print(pork)
