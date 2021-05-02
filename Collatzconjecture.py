num=int(input("Enter any number"))
if (num%2==0):
    while(num!=1):
        num=num//2
        print(num,"\n")
elif(num%2!=0):
    num=3*num+1
    while(num!=1):
        num=num//2
        print(num,"\n")
else:
    print("!!!INVALID INPUT!!!")
