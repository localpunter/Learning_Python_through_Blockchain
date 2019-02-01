class Car:
    top_speed = 100
    warnings = []

    def drive(self):
        print('I am driving but certainly not faster than {}'.format(self.top_speed))

car1 = Car()
car1.drive()

# Car.top_speed = 200
car1.warnings.append('New warning')

car2 = Car()
car2.drive()
print(car2.warnings)

car3 = Car()
car3.drive()
print(car3.warnings)