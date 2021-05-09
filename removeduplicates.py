def deldup(l1):
    l2=[]
    for j in l1:
        if j not in l2:
            l2.append(j)
    print(l2)           
n=int(input("Enter range:"))
l1=[]
l2=[]
for i in range(n):
    a=int(input("Enter number:"))
    l1.append(a)
deldup(l1)

