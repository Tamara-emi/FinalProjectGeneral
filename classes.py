'''class Info:
    def name(self):
        return "Bridget"

    def age(self):
        print(19) 

me = Info()

print(me.name())

me.age()'''


'''class Car:

    def __init__(self, year_model, make,speed = 0):
        self.year_model = year_model
        self.make =  make
        self.speed = speed


    def accelerate(self):
        self.speed = self.speed + 5
        return self.speed

    def brake(self):
        self.speed = self.speed - 5
        return self.speed

    def get_speed(self):
        return self.speed


mercedes = Car(2022,'benz')

for i in range(5):

    mercedes.accelerate()
    print(mercedes.get_speed())'''
class Vehicle:
     def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
     
     def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"  


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(self, name, max_speed, mileage)
    def data(self):
        return f'Name: {self.name} Speed : {self.max_speed} Mileage: {self.mileage}'
    
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

bus1 = Bus("School Volvo", 180 , 12)  
print(bus1.data())




