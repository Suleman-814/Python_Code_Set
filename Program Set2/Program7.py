#4 WAP to find user number is divisible by 10,20 or not 

divNum=int(input("Enter a Number: "))
if divNum%10==0 and divNum%20!=0:
    print(f"{divNum} is divisible by 10 but not by 20")
elif divNum%20==0 and divNum%10!=0:
    print(f"{divNum} is divisible by 20 but not by 10 ")
elif divNum%10 or divNum%20==0:
     print(f"{divNum} is divisible by 10 and 20 ")
else:
       print(f"{divNum} is not divisible by 10 and 20")
print("Thank You!")  