#class definition
#class Student:
#    def __init__(self,name,gender):
#        self.name = name
#        self.gender = gender

#    def details(self):
#        return "kimc student"
    
#object creation
#Student1 = Student("Alicia", "female")
#Student2 = Student("Alvin", "male")

#Acessing object properties and methods
#print(f"{Student1.name} is a  {Student1.gender}  {Student1.details()}")
#print(f"{Student2.name} is a {Student2.gender} {Student2.details()}")

#using inheritance
class Car:
    def __init__(self,name):
        self.name = name

    def electric(self):
        pass

#inheritance
class Tesla (Car):
    def electric(self):
        return (f"{self.name}, is an electric car")
    
#polymorphism
USA = [
    Tesla("CyberTruck")
]

for car in USA:
    print(car.electric())

    


