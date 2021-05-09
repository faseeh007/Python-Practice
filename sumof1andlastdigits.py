n=int(input("Enter number to add sum of first and last digits:\n"))
sum=0
a=n%10
sum=sum+a
while(n!=0):
    n=n//10
    if n<10:
        sum=sum+n
print(sum)
