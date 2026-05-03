#Question 2

list=[]
evenlist= [y for y in range(0,20) if y%2==0]
list.extend(evenlist)
print(list)