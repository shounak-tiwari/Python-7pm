def home():
    print("hello!")

class demo:
    def __init__(self,name,last,age):
        self.name =name
        self.last = last
        self.age = age
    
    def fullname(self):
        print("Name of student : ",self.name,self.last)
    

demo = demo('x','y',00)