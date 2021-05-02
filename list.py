n=int(input("Enter number of elements in an array:\n"))
l1=[]
print("Enter array elements")
for i in range(n):
    a=int(input())
    l1.append(a)
print("Given list is",l1)
l1.sort()
print("Third largest number is",l1[2])
