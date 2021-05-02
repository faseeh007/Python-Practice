n=int(input("Enter price:"))
m=int(input("Enter Quantity:"))
print("Price=",n,"\t Quantity=",m)
a=n*m
x=a
if a>1000:
    a=a-(a/10)
    print("Amount=",a,"\tDiscount=",x/10)
else:
    print("Amount=",a)
