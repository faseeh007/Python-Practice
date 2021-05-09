a=[]
n=int(input("Enter number of elements:\n"))
print("Enter elements:")
for x in range(n):
    y=int(input())
    a.append(y)
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                t=a[i]
                a[i]=a[j]
                a[j]=t
print("Sorted list=",a)