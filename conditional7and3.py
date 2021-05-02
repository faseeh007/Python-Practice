print("started")
x=1
a=1
for x in range(100):
    if (x%3==0 or x%7==0):
        if (x%3==0 and x%7==0):
            continue
        print(x)
        x=x+1
print("done")
