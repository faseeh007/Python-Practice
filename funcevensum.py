def even(n,m,l1):
    sum=0
    for i in range(n,m):
        if i%2==0:
            l1.append(i)
    for ia in l1:
        sum=sum+ia
    print(sum)
    #return sum

n=int(input("Enter starting number:"))
m=int(input("Enter ending value:"))
l1=[]
even(n,m,l1)
