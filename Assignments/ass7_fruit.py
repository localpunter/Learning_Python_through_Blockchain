from assignment_7 import Food

class Fruit(Food):
    def clean(self):
        print("\nI always wash my fruit before I eat it!")


fruit1 = Fruit("Granny Smith", "apple")
fruit1.clean()
fruit1.eat2()
