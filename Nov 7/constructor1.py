class Student_record():
    # constructor 
    def __init__(self):
        print("this is student constructor")
    def __del__(self):
        print("distructor is executed from student")
class Demo():
    # constructor 
    def __init__(self)->None:
        print("this is demo constructor ")
    def __del__(self)->None:
        print("This is demo distructor ")
# student record
Object_1 = Student_record()
Object_2 = Student_record()
# demo
Demo_1 = Demo()
Demo_2 = Demo()
x =10
print(x)