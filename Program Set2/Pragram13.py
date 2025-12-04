age=int(input("Enter Your Age :"))
if age==0:
    print("age can not be zero")
elif age<0:
    print("No negative age")
elif age>60:
    print("You are senior citizen")
elif age<=60 and age>=15:
    print("You are not  senior citizen")
elif age<15:
    print("You are children")
else:
    print("you are a baby")