n=int(input("Sum of evens upto which number?\n"))
sum=0
for x in range(n+1):
    if x%2==0:
        sum=sum+x
print("Sum=",sum)
