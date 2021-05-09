n=int(input("Enter number to add sum of digits:\n"))
sum=0
while(n>0):
    a=n%10
    if(a%2!=0):
        sum+=a
    n=n//10
print(sum)
