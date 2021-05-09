n=int(input("Enter number to add sum of digits:\n"))
sum=0
while(n>0):
    a=n%10
    n=n//10
    sum=sum+a
print(sum)
