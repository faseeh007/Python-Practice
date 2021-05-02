a=int(input("Enter number:\n"))
sum=0
x=a
while(a>0):
    d=a%10
    sum=sum+d*d*d
    a=a//10
if (sum==x):
    print("Armstrong number")
else:
    print("Not Armstrong number")
