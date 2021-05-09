import math
print("ax**2+bx+c")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
D=b**2-4*a*c
root1=(-b+math.sqrt(D))/2*a
root2=(-b-math.sqrt(D))/2*a
if D<0:
    print("Complex Roots")
else:
    print("Root 1:",root1)
    print("Root 2:",root2)
