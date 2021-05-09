ft=int(input("Enter the value in feet:\n"))
print("Enter to which units it is to be converted?\nTo\n1.metres\n2.inches\n3.cm\n")
n=int(input("Enter 1/2/3:\n"))
if n==1:
    m=0.3048*ft
    print(ft,"feet = ",m,"metres")
elif n==2:
    inch=12*ft
    print(ft,"feet = ",inch,"inches")
elif n==3:
    cm=30.48*ft
    print(ft,"feet = ",cm,"centimetres")
else:
    print("!!!INVALID INPUT!!!")
