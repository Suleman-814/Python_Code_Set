# WAP to print even & odd number from list and to print sum of them using while loop



list=[10,11,13,14,16,17,33,35,37,38,20,40,50,60,99,98,97]
i=0
sum=0
#oddlist=[]
while i<len(list):
   # print(i, list[i])
    if list[i]%2==0:
        #oddlist.append(list[i])
        print(list[i])
        sum+=list[i]
    i+=1    
#print(oddlist)
print("Sum:",sum)

#######################################################
list=[10,11,13,14,16,17,33,35,37,38,20,40,50,60,99,98,97]
i=0
sum=0
#oddlist=[]
while i<len(list):
    #print(i, list[i])
    if list[i]%2!=0:
        #oddlist.append(list[i])
        print(list[i])
        sum+=list[i]
    i+=1    
#print(oddlist)
print("Sum",sum)