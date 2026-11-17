# for i in range(5)print("Good Morning Students")
# i=1
# while i<=5:
#     print("good morning students")
#     i+=1

# def great():
#     print("Hello students")
#     print("welcome to python programming")
# great()

# def add(a,b):
#     result = a+b
#     print(result)
# add(10,20)
# add(100,200

# students = ["Dingi","Dinga","Nibbi","Nibba"]
# print (students[3])
# students = ["Dingi","Dinga","Nibbi","Nibba"]
# students.append("Ding")
# students.remove("Dinga")
# students.insert(3,"Dinga")
# print(students)

# students_details = ("nibba", 23, "89", "True")
# print(students_details[0])

# students_details = {"name":"SRIJA", "age":20, "marks":97, "is_passed":True, "usn":"1gd24cs149"}
# students_details["course"] = "python"
# print(students_details["age"])
# print(students_details["course"])
# print(students_details["usn"])
# print(students_details["marks"])
# print(students_details["is_passed"])

##################### OOPS ########################

# class student:
#     def __init__(self,name, age, usn, marks):
#         self.name = name
#         self.age = age
#         self.usn = usn
#         self.marks = marks
        
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("USN:", self.usn)
#         print("Marks:", self.marks)
# s1=student("SRIJA", 20, "1gd24cs149", 97)
# s2=student("JAGDISH", 22, "1gd24cs001", 79)
# s1.display()
# s2.display()

#################### MINI PROJECT ####################

# class student:
#     def __init__(self):
#         self.marks = 0
        
#     def set_marks(self, marks):
#         self.marks = marks
        
#     def show_marks(self):
#         print("Marks:", self.marks)
        
# s1 = student()
# s1.set_marks(97)
# s1.show_marks()

# class father:
#     def House(self):
#         print("Father has a house")
# class son(father):
#     def Car(self):
#         print("Son has a car")  
# s=son()
# s.House()
# s.Car()

#################### MULTI LEVEL INHERITANCE ####################

# class grandfather:
#     def House(self):
#         print("Grandfather has a land")
        
# class father(grandfather):
#     def Car(self):
#         print("Father has a car")

# class son(father):
#     def Bike(self):
#         print("Son has a bike")

# s=son()
# s.House()
# s.Car()
# s.Bike()

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class cat(Animal):
#     def sound(self):
#         print("Cat meows")
# animals = [Dog(), cat(), Animal()]
# for animal in animals:
#     animal.sound()

from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class upi(payment):
    def pay(self, amount):
        print(f"Payment of {amount} done using UPI")
class card(payment):
    def pay(self,amount):
        print(f"Payment of {amount} done using card")
p1=upi()
p2=card()
p1.pay(1000)
p2.pay(2000)