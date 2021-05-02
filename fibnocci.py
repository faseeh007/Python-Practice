n=int(input("Enter number:\n"))
a=0
b=1
print(a)
for i in range (0,n-1):
    a,b=b,a+b
    print(a)
