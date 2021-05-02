class test:
    n=1
    def _init_ (self):
        print("In constructor",self.n)
    def disp(self,val):
        self.n=val
        print("disp called",self.n)
t4=test()
t4.disp(10)
        
