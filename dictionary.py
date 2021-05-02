"""
Write a Python code to store the name and age of the employee of an organisation 
in the dictionary from user, where name is "Key" and age is the "value".
Find the number of employees whose age is greater than 25 and display them.

"""
n=int(input("Enter number of persons:"))
l1={}
count=0
for i in range(n):
    name=input("enter name:")
    age=int(input("enter age:"))
    l1[name]=age
print("Employees age greater than 25")
for k,v in l1.items():
    if v>25:
        count+=1
        print(k,v)
print("count =",count)
