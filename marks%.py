a=int(input("Enter marks 1:"))
b=int(input("Enter marks 2:"))
c=int(input("Enter marks 3:"))
d=int(input("Enter marks 4:"))
e=int(input("Enter marks 5:"))

percent=(a+b+c+d+e)//5
print("Percentage = ",percent,"%")
if(percent>=90):
    print("Grade A")
if(90>percent>=80):
    print("Grade B")
if(80>percent>=70):
    print("Grade C")
if(70>percent>=60):
    print("Grade D")
if(60>percent>=50):
    print("Grade E")
if(50>percent>=40):
    print("Grade F")
