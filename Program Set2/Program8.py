#WAP to find user number is divisible by 3,5,7 or not

DNum=int(input("Enter a Number:"))
if DNum%3==0 and DNum%5!=0 and DNum%7!=0:
    print(f"{DNum} is divisible by 3 but not by 5 & 7")
elif DNum%5==0 and DNum%3!=0 and DNum%7!=0:
    print(f"{DNum} is divisible by 5 but not by 3 & 7 ")
elif DNum%7==0 and DNum%3!=0 and DNum%5!=0:
    print(f"{DNum} is divisible by 7 but not by 3 & 5 ")    
elif DNum%3==0 or DNum%5==0 and DNum%7!=0 :
     print(f"{DNum} is divisible by 3 & 5 not by 7 ")
elif DNum%5==0 or DNum%7==0 and DNum%3!=0 :
    print(f"{DNum} is divisible by 5 & 7 not by 3 ")  
else:
       print(f"{DNum} is not divisible by 3,5 & 7")
print("Thank You!")  