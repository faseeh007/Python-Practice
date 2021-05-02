x=int(input("Enter any number to find the divisors:"))
y=[]
for z in range(1,x+1):
    if x%z==0:
        y.append(z)
print("The divisors of",x,"are",y)
