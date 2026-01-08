#WAP to find odd number till 100 using fir loop and while loop.

for i in range(0,101):
    if i%2!=0:
        print(i, end="\t")

print( "#############################################################")    
i=0
while i<101:
    if i%2!=0:
        print(i, end="\t")
    i+=1
