#WAP to enter a number till termination condition meet and print sum and addto list using while loop

sum=0
list1=[]
while True:
    y=int(input("enter a number"))
    if y == 0:
        break
    list1.append(y)
    sum+=y
print(sum)
print(list1)    