#creating a class
class Vehicle():
    #initialize the class with parameters
    def __init__(self, name, color, brand, engineSize):
        self.name = name
        self.color = color
        self.brand = brand
        self.engineSize = engineSize
    #creating a method to show the parameters values
    def showDetails(self):       
        print(self.name,self.color,self.brand, self.engineSize)
#Create a loop that ask the user to inpunt the different 
#parameter and then create the object with that parameter
#and print out the values
for i in range(1,5):
    name = input ("Enter name of vehicle: ")
    color = input ("Enter color of vehicle: ")
    brand = input ("Enter brand of vehicle: ")
    engineSize = input ("Enter the size of the engine: ")
    i = Vehicle (name, color, brand, engineSize)
    i.showDetails()
