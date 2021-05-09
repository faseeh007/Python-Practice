import sys
import os
user1=str(input("What's your name?\n"))
user2=str(input("What's your name?\n"))
print(user1,"Enter")
x=str(input("rock|paper|scissors?\n"))
os.system('clear')
print(user2,"Enter")
y=str(input("rock|paper|scissors?\n"))
if(x==y):
    print(user1,"and",user2,"had a tie game")
elif(x=='rock' and y=='paper'):
    print(user2,"won the match")
elif(x=='rock' and y=='scissors'):
    print(user1,"won the match")
elif(x=='paper' and y=='rock'):
    print(user1,"won the match")
elif(x=='paper' and y=='scissors'):
    print(user2,"won the match")
elif(x=='scissors' and y=='rock'):
    print(user2,"won the match")
elif(x=='scissors' and y=='paper'):
    print(user1,"won the match")
else:
    ("Entered input is wrong")
sys.exit
