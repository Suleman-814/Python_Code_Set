# WAP to find even number and to get sum of even no. using for loop.


sum=0
for i in range(0,101):
    if i%2==0:
        print(i, end="\t")
        sum+=i
print("sum of natural number is =",sum,end="\t")    
