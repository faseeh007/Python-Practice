def computeJ(w1,w2):
    j=w1**2+w2**2+4*w1-6*w2-7
    return j
def computew1(oldw1,oldw2,alpha):
    return(2*oldw1+4)
def computew2(oldw1,oldw2,alpha):
    return(2*oldw2-6)
w1=float(input("Enter w1:\n"))
w2=float(input("Enter w2:\n"))
alpha=float(input("Enter alpha:\n"))
n=int(input("Enter number of iterations:\n"))
print("\n")
for i in range(n):
    j=computeJ(w1,w2)
    print(i+1,"iteration")
    print('\nw1=',w1)
    print('w2=',w2)
    print('j=',j,"\n")
    oldw1=w1
    w1=oldw1-alpha*computew1(w1,w2,alpha)
    oldw2=w2
    w2=oldw2-alpha*computew2(w1,w2,alpha)
