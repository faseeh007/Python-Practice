def sal(list):
    s=0
    for i in list:
        if i>=30000:
            s=s+i
            return s
list=[25000,30000,32000,31000]
a=[]
print(sal(list))

