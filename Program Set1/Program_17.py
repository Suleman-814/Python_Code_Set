#WAP to Print Natural Numbers from 1 to 10 and Find Their Sum, and Also Print & Sum Even Numbers from a List

sum=0
i=1
while i<11:
    print(i)
    sum+=i
    i+=1
    #sum+=i
print("sum of natural number is =",sum)

list=[10,11,13,14,16,17,33,35,37,38,20,40,50,60,99,98,97,100]
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

