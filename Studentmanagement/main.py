# class Student:
#     def __init__(self, name, age, usn, marks):
#         self.name = name
#         self.age = age
#         self.usn = usn
#         self.marks = marks
        
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("USN:", self.usn)
#         print("Marks:", self.marks)
#         print("-----------------------------")
        
# class StudentManagement:
#     def __init__(self):
#         self.students = []
        
#     def add_student(self):
#         usn = input("Enter USN: ")
        
#         # Check if student already exists
#         for student in self.students:
#             if student.usn == usn:
#                 print("Student already exists")
#                 return
            
#         name = input("Enter student's name: ")
#         try:
#             age = int(input("Enter student's age: "))
#             marks = float(input("Enter student's marks: "))
#         except ValueError:
#             print("Invalid input for age or marks. Please enter numeric values.")
#             return
        
#         new_student = Student(name, age, usn, marks)
#         self.students.append(new_student)
#         print("Student added successfully")
        
#     def view_students(self):
#         if len(self.students) == 0:
#             print("No students found")
#             return
#         for student in self.students:
#             student.display()
        
#     def search_student(self):
#         usn = input("Enter USN to search: ")
#         for student in self.students:
#             if student.usn == usn:
#                 student.display()
#                 return
#         print("Student not found")
        
#     def delete_student(self):
#         usn = input("Enter USN to delete: ")
#         for student in self.students:
#             if student.usn == usn:
#                 self.students.remove(student)
#                 print("Student deleted successfully")
#                 return
#         print("Student not found")
    
# app = StudentManagement()

# while True:
#     print("\n-------------- Student Management System -----------------")
#     print("1. Add Student")
#     print("2. View Students")
#     print("3. Search Student")
#     print("4. Delete Student")
#     print("5. Exit")
    
#     choice = input("Enter your choice: ")
    
#     if choice == "1":
#         app.add_student()
#     elif choice == "2":
#         app.view_students()
#     elif choice == "3":
#         app.search_student()
#     elif choice == "4":
#         app.delete_student()
#     elif choice == "5":
#         print("Exiting program. Goodbye!")
#         break
#     else:
#         print("Invalid choice, please try again.")
        
    