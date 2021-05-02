n=int(input("Enter any number to check whether it is a palindrome or not : \n"))
m=n
rev=0
while (n!=0):
    rev=rev*10+n%10
    n=n//10
if rev==m:
    print(m,"is a palindrome")
else:
    print(m,"is not a palindrome")
print("Task completed successfully")
    
