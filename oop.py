class MyClass:
    '''This is my DocString
Example of Class Variable a,Instance variable a
Instantiation,Call Function using object of class
Display'''
    a=10 #Class Variable
    def __init__(self): #Class Constructor
        self.a=100 #Instance Variable
        print("Instance variable a=",self.a)
    def func(self):#Method in a class
        print("Hello")
#Display Class variable
print("Using class name class variable a=",MyClass.a)
Mc1=MyClass() #instantiation
#get address of func() method
print(MyClass.func)
Mc1.func() #Function call using class object Mc1
print(MyClass.__doc__) #Prints the docstring
print(Mc1.a)
