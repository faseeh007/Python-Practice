x=int(input("enter num"))
ls=[]
l=len(ls)-1
ls1=[]
while(l>=0):
    ls1.append(ls[l])
    l=l-1
res=[ls1[i]+ls1[i] for i in range(len(ls1))]
    

