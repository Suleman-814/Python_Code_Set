# WAP to print even & odd number from list and to print sum of them using for loop

list=[10,11,13,14,16,17,33,35,37,38,20,40,50,60,99,98,97]
sum= 0
for i in list:
    if i%2==0:
        print("even no",i)
        sum+=i
print('Sum of even number:',sum)

############################################

list=[10,11,13,14,16,17,33,35,37,38,20,40,50,60,99,98,97]
sum= 0
for i in list:
    if i%2!=0:
        print("even no",i)
        sum+=i
print("Sum of odd number:",sum)  
