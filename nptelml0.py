def compute_j(w1,w2):
    j= w1**2 +w2**2 +4*w1-6*w2-7
    return j
def compute_gradient_w1(w1,w2):
    return(2*w1+4)
def compute_gradient_w2(w1,w2):
    return(2*w2-6)
w1 = 5
w2 = 5
Alpha = 0.3
for i in range(1000):
     j = compute_j(w1,w2)
     print("iteration ",i+1)
     print('w1=',w1)
     print('w2=',w2)
     print('j=',j)
     oldw1=w1
     w1=w1-Alpha*compute_gradient_w1(w1,w2)
     w2=w2-Alpha*compute_gradient_w2(oldw1,w2)
     
     
     
     
     
     
     