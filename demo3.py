import math
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
print("under root >=0",(math.sqrt(pow(b,2)-4*a*c))>=0)
print("is a !=0",a!=0)
print(-b+(math.sqrt(pow(b,2)-4*a*c)/2*a))
print(-b-(math.sqrt(pow(b,2)-4*a*c)/2*a))
