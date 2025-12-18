#WAP to print list and print the table of number entered

for i in range(-1,1):
    print(i)

list=["C","C++","JAVA","JAVASCRIPT","PYTHON","PHP","KOTLIN"]
for i in range(len(list)):
    print(i, list[i] ,end=",")
    #print(list[i])

t=int(input("Enter a Number:"))
for i in range (1, 11):
    print(t,"x",i,"=",t*i)