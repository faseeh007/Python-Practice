a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if(a>b and a>c):
    print("a is greatest")
elif(b>a and b>c):
    print("b is greatest")
elif(c>a and c>b):
    print("c is greatest")
else:
    print("All are equal")
