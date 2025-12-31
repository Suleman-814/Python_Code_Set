#WAP to enter a number till termination condition meet and print sum and addto list using for loop

list=[]
sum=0
for i in iter (int,1):
    x= int(input("enter a number"))
    if x==0:
        break
    list.append(x)
    sum+=x 
print(sum)
print(list) 



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