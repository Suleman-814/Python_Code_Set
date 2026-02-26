#WAP to Separate Even and Odd Numbers from a Given List

array_given=[10,20,30,40,50,60,70,80,90,100,105,115,125,135,145,155,165,175,185,195]
evenlist=[]
oddlist=[]

for i in array_given:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("Even list is:", evenlist,"\nOdd list is:",oddlist)
