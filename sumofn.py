"""
Write a python program to display sum of first n numbers

Sample input & Output:
enter n value                                                                                                           
10                                                                                                                      
sum of first n numbers= 55  
"""
# read n value
# calculate sum of first n numbers using loop
#display sum of first n numbers
sum=0
n=int(input("enter n value\n"))
while(n>0):
    sum=sum+n
    n=n-1
print("sum of first n numbers= ",sum)
