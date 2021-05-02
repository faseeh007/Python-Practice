class sum:
    sum=0
    def add(self,n):
        #n=10
        while(n!=0):
            self.sum+=n
            n-=1
        return self.sum
x=sum()
n=int(input("Enter a number to find sum of natural numbers:\n"))
y=x.add(n)
print(x.sum)
