# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe()” method
# (which prints “name” and “kind” in a sentence).


class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        print('My name is {} and I belong to the kind of {}'.format(
            self.name, self.kind))

    def __repr__(self):
        return 'Name: {}, Kind: {}'.format(self.name, self.kind)


# banana = Food('Banana', 'Fruits')
# banana.describe()


# 2) Try turning describe() from an instance method into a class and a static method. Change it back to an instance method thereafter.

# class Food:
#       def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind

#     @staticmethod
#     def describe(name, kind):
#         print('My name is {} and I belong to the kind of {}'.format(
#             name, kind))

# Food.describe('Banana', 'Fruit')

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”.
# Add a “cook()” method to “Meat” and “clean()” to “Fruit”.

class Meat(Food):

    def __init__(self, name):
        super().__init__(name, 'meat')

    def cook(self):
        print('I am cooking')


class Fruit(Food):

    def __init__(self, name):
        super().__init__(name, 'fruit')

    def cleaning(self):
        print('I am cleaning')


banana = Fruit('banana')
banana.describe()
banana.cleaning()


pork = Meat('pork')
pork.describe()
pork.cook()


# 4) Overwrite a “dunder” method to be able to print your “Food” class.
print(banana)
print(pork)
