import random
number=random.randint(1,9)
guess=0
count=0
while guess!=number and guess!="exit":
    guess=int(input("What's your guess?"))
    if guess=="exit":
        break
    count+=1
    if guess>number:
        print("Too High")
    if guess<number:
        print("Too Low")
    if guess==number:
        print("You are right\n You have taken",count,"chance(s)")
