class vechile:
    def __init__(self):
        self.nos = input("Enter the number seats :")
        self.maxspeed = float(input("maximum speed : "))
        self.price = float(input("Price : "))
        self.model_no = input("Model number : ")
    
    def display(self):
        print("No of seats : ",self.nos)
        print("Maximum speed : ",self.maxspeed)
        print("Price of vechile : ",self.price)
        print("Model number : ",self.model_no)
    

class Bike(vechile):
    def __init__(self):
        super().__init__()
        self.cylinders = input("No of cylinders : ")
        self.Torque = input("Torque genreted by bike : ")
        self.rpm = int(input("Higest rpm of bike : "))
    
    def show(self):
        vechile.display(self)
        print("No of culiders : ",self.cylinders)
        print("Torque genrated by biike : ",self.Torque)
        print("Maximum rpm of bike : ",self.rpm)
    


Obj_Bike = Bike()

Obj_Bike.show()