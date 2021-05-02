class student:
    sn='abc'
    sr='123'
    def __init__(self,n,r):
        self.sn=n
        self.sr=r
    
    def disp(self,n,r):
        print("Student name: ",self.sn)
        print("Student roll number: ",self.sr)
x=input("enter name:")
y=input("enter roll number:")
tst=student(x,y)
tst.disp(x,y)        
