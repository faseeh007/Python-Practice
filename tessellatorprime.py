n=int(input("Enter start value:"))
m=int(input("Enter end value:"))
for i in range(n,m):
    for j in range(2,i):
       if i%j==0:
           break
    else:
        print(i,end=" ")
