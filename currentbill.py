n=int(input("Enter units of Electricity:"))
if n<=50:
    cost=n*0.5
    #price=(cost+(cost/5))
    #print("Cost=",price)    

elif(50<n<=150):
    cost=(50*0.5)+(n-50)*1.25
    
    #print("Cost=",price)    

elif(150<n<=250):
    cost=(50*0.5)+(n-50)*1.25+(n-100)*1.75
    #price=(cost+(cost/5))
    #print("Cost=",price)    

elif(n>250):
    cost=(50*0.5)+((n-50)*1.25)+((n-100)*1.75)+((n-250)*2.5)
price=(cost+(cost/5))
print("Cost without surplus:",cost)
print("Cost=",price)    
