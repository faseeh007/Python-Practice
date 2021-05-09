import math
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
p1=math.pow(b,2)
r1=(-b+(math.sqrt(p1-4*a*c)))/2*a
r2=(-b-(math.sqrt(p1-4*a*c)))/2*a
print("root 1=",r1)
print("root 2=",r2)
