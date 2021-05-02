class test:
    n=1#class variable should be initialized
    def disp(self):#member function
        val=200#instance variable
        print("disp called. Value of n:",self.n)
        print("in disp local variable val:",val)
    def __init__(self):#constructor
        print("Constructor called")
tst=test()#tst is instance of class text
tst.disp()

