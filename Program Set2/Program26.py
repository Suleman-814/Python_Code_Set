# WAP to find even number and to get sum of even no. using while loop.



sum=0
i=0
while i<101:
    if i%2==0:
        print(i, end="\t")
        sum+=i
    i+=1 
print("sum of natural number is =",sum,end="\t") 