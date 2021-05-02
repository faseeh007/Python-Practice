"""
A number is said to be "magic number", 
if sum of all the digits of the number is equal to 1 and 
the number itself a single digit number
( i.e keep on adding the digits of a number till it becomes a single digit number).
If the sum is one then the number is a magic number, otherwise not.

For example consider number 55
  Then ,5+5=10
        1+0=1
55 is a magic number


case 1:
Sample input:
Enter a number:64 
sample output:
The number is magic

case 2:
Sample input:
Enter a number:105
Sample output:
The number is not magic 

"""
n=int(input("Enter a number:"))
sum=0
x=0
y=n
while(n>0):
    a=n%10
    sum=sum+a
    n=n//10
if sum>9:
    while (sum>1):
        if sum%10==0:
            p=sum//10
            x=x+p
            sum=sum//10
        else:
            b=sum%10
            x=x+b
            sum=sum//10

    if x==1:
        print("The number is magic")
    else:
        print("The number is not magic")
else:
    print("The number is not magic")



















