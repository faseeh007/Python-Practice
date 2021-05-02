'''write a python program to find maximum value of given n numbers
enter n value                                                                                                           
3                                                                                                                       
enter a number                                                                                                          
3                                                                                                                       
enter a number                                                                                                          
2                                                                                                                       
enter a number                                                                                                          
1                                                                                                                       
maximum value= 3 
'''

max=0
n=int(input("enter n value\n")) 
while (n>0):
    num=int(input("enter a number\n")) 
    if num>max:
        max=num
    n=n-1
print("maximum value=",max)
