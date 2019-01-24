from vehicle import Vehicle

class Car(Vehicle):
    # top_seed = 100
    # warnings = []

    def brag(self):
        print("Hey! Look how cool my car is!!")


car1 = Car()
car1.drive()


# Car.top_seed = 200
car1.add_warning("Low Oil")
# car1.get_warnings().append([])
# print(car1.__dict__)
print(car1)

car2 = Car(200)
car2.drive()
print(car2.get_warnings())

car3 = Car(250)
car3.drive()
print(car3.get_warnings())


