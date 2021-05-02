class book:
    bc=0
    bt='title'
    ba='author'
    bid='xy123'
    def __init__(self,x,y,z):
        self.bid=x
        self.bt=y
        self.ba=z
        book.bc+=1
    def disp(self):
        print("Book id is ",self.bid)
        print("Book title is ",self.bt)
        print("Book author is ",self.ba)
        print("Book count is",self.bc)
x=book(100,"let us c","y kanetkar")
x.disp()
y=book(20,'python','rossum')
y.disp()
z=book(30,'cpp','yash')
z.disp()
