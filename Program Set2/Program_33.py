list=[]
while True:
    num=int(input("enter a number"))
    if num==0:
        print("no 0 allowed") 
        break
    else:
        list.append(num)
        print(f"Added {num} to the list")
print(f" The final list is: {list}")
        
