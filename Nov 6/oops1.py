class Student_record:
    def input(self):
        self.name = input("Enter the Name of student : ")
        self.rollnumber = input("Enter the Roll number of student : ")
        self.contact = input("Enter the contact number : ")

    def display(self):
        print("The name of student : ",self.name)
        print("The roll number of student : ",self.rollnumber)
        print("The contact of student : ",self.contact)


Payal = Student_record()
Payal.input()
Payal.display()