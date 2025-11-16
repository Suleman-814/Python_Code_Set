#WAP to find user number is divisible by 3,5 or not

divNum=int(input("Enter a Number: "))
if divNum%3==0 and divNum%5!=0:
    print(f"{divNum} is divisible by 3 but not by 5")
elif divNum%5==0 and divNum%3!=0:
    print(f"{divNum} is divisible by 5 but not by 3 ")
elif divNum%3 or divNum%5==0:
     print(f"{divNum} is divisible by 5 and 3 ")
else:
       print(f"{divNum} is not divisible by 3 and 5")
print("Thank You!")