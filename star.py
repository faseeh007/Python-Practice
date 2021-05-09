n=int(input("Enter no. of rows"))
i=1
y="* "
if n>=2:
    while(i<=n):
        print(y*i,"\n")
        i+=1
else:
    print("Enter any num more than or equal 2")
