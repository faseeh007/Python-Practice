num=int(input("enter number:\n"))
count=0
for i in range(2,num-1):
    if num%i==0:
        count=1
        break
    else:
        count=0
if count==0:
    print("prime")
elif count==1:
    print("not prime")
