def fact(n):
    if(n>1):
        return(n*fact(n-1))
    else:
        return 1
num1=int(input("Enter the number to find factorial:"))
print("factorial=",fact(num1))
