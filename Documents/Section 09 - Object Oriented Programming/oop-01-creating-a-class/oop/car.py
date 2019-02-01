class Car:
    top_speed = 100

    def drive(self):
        print('I am driving but certainly not faster than {}'.format(self.top_speed))

car1 = Car()
car1.drive()