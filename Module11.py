#Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each publication
# has a name. Each book also has an author and a page count, whereas each magazine has a chief editor. Also write the
# required initializers to both classes. Create a print_information method to both subclasses for printing out all
# information of the publication in question. In the main program, create publications Donald Duck (chief editor Aki Hyyppä)
# and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both publications using the methods
# you implemented.
'''
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page):
        super().__init__(name)
        self.author = author
        self.page = page

    def print_information(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

publication1 = Magazine("Donald Duck", "Aki Hyyppä")
publication2 = Book("Compartment No. 6", "Rosa Liksom", 192)

publication1.print_information()
publication2.print_information()
'''
#Extend the previously written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have the
# capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as
# their property. Write initializers for the subclasses. For example, the initializer of electric cars receives the
# registration number, maximum speed and battery capacity as its parameter. It calls the initializer of the base class
# to set the first two properties and then sets its capacity. Write a main program where you create one electric car
# (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them
# drive for three hours and print out the values of their kilometer counters.

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def set_speed(self, speed):
        self.current_speed = min(speed, self.maximum_speed)

    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)


electric_car.set_speed(130)
gasoline_car.set_speed(125)


electric_car.drive(2)
gasoline_car.drive(4)


print(f"Electric Car (Reg. {electric_car.registration_number}) - Kilometers Driven: {electric_car.travelled_distance} km")
print(f"Gasoline Car (Reg. {gasoline_car.registration_number}) - Kilometers Driven: {gasoline_car.travelled_distance} km")