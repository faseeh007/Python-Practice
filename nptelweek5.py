A = list(map(int, input().split()))
mylist=[]
for i in range(len(A)):
    for j in range(1, len(A)-i):
        # swap if prev value is less than current value
        # change < to > to reverse the order
        if mylist[j-1] < mylist[j]:
            # do a tuple swap
            (mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
print(mylist)
