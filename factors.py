n=int(input("Enter any number to find factors:"))
for x in range(1,n+1):
    if (n%x==0):
        print(x,end=" ")
