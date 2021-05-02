fi=[19,1,1,22,19,88,34,29]
print(fi)
result=filter(lambda x:x%2!=0,fi)
print("the list of numbers not divisible by 2 are",list(result))
result1=filter(lambda x:x%2==0,fi)
print("the list of numbers divisible by 2 are",list(result1))
