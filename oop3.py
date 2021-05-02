class Complex:
    i=0
    r=0
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
compObj=Complex(3.0,-4.5)
print("Real part",compObj.r,"\nImaginary part",compObj.i)
