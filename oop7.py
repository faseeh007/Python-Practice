class factorial:
    num=0
    def __init__(self,n):
        self.num=n
    def func(self,n,x):
        p=1
        while(n!=0):
            p=p*n
            n-=1
        print("Factorial of",x,"is",p)
n=int(input("Enter a number:"))
x=n
tst=factorial(n)
tst.func(n,x)
