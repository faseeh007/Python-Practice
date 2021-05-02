def changeme(mylist):
    mylist.append(1);
    print("Values inside the functions:",mylist)
    return
mylist=[10,20,30]
changeme(mylist)
print("Values outside the function:",mylist)