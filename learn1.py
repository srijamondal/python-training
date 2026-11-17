# college = "Gopalan college of engineering"
# print(college)
# usn = "1Gd24CS149"
# print(usn)
a=10
b=20
# print(a+b)
# print(a/b)
# print(a-b)
# print(a==b)
# print(a>b)
# print(a<b)
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("pass")
else:
    print("fail ")
    
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A grade")
elif marks >= 80:
    print("B grade")
else:
    print("C grade")

# Enter marks for three students and print their total
student1_marks = int(input("Enter marks for student 1: "))
student2_marks = int(input("Enter marks for student 2: "))
student3_marks = int(input("Enter marks for student 3: "))

total_marks = student1_marks + student2_marks + student3_marks
print("Total marks of the three students:", total_marks)
