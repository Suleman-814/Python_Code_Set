#WAP to check whether a student is eligible to sit in exam or not.


T_A=int(input("Enter Total number of lectures attended"))
T_L=int(input("Enter Total number of lectures taken:"))
per= (T_A*100)/T_L
print("Total attendence Percentage is :", per)
if per>0:
    if per<75:
        print("You are not eligible for appearing in exam")
        print("Total attendence Percentage is :", per)
else:
    print("No negative value")
