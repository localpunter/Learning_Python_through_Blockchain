class Car:
    # top_speed = 100
    # warnings = []
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.warnings = []

    def drive(self):
        print('I am driving but certainly not faster than {}'.format(self.top_speed))

car1 = Car()
car1.drive()

# Car.top_speed = 200
car1.warnings.append('New warning')

car2 = Car(200)
car2.drive()
print(car2.warnings)

car3 = Car(250)
car3.drive()
print(car3.warnings)