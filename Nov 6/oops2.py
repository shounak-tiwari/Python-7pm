class Student_record:
    def input(self):
        self.name = input("Enter the name of student ")
        self.contact = input("Enter the contact number : ")
    
    def display (self):
        print("The Name of student : ",self.name)
        print("The contact of student : ",self.contact)



Hasan = Student_record()
Hasan.input()
Faiz = Student_record()
Faiz.input()
Kaif = Student_record()
Kaif.input()
Aman = Student_record()
Aman.input()
Faiz.display()