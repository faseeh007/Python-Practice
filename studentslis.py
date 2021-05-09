marks=[]
names=[]
avg1=[]
num=int(input("Enter the number of students:\n"))
num1=int(input("Enter the number of subjects:\n"))
for i in range(1,num+1):
    name=str(input("Name of students %d: "%i))
    names.append(name)
    marka=[]
    for j in range(1,num1+1):
        mark=int(input("Enter subject %d marks:"%j))
        marks.append(mark)
    tot=sum(int(j) for j in marks)
    print("Student",i,"marks are:")
    print(marks)
