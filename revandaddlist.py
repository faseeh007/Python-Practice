n=int(input("Enter number of elements in an array"))
l1=[int(i) for i in input().split()]
l2=list(reversed(l1))
a=[l1[m]+l2[m] for m in range (len(l1))]
for b in a:
    print(b,end='')
