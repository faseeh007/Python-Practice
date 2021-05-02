import math
x,y,z=map(int,input().split())
d1=z
d2=math.sqrt(2)*z
t1=x/d1
t2=x/d2
if(t1>t2):
  print("Walk")
else:
  print("Cab")
