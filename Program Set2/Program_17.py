#WAP to check whether a student is eligible to sit in exam or not using conditions.


T_A=int(input("Enter Total number of lectures attended:"))
T_L=int(input("Enter Total number of lectures taken:"))
if T_A<0 or T_L<0 and T_L<T_A :
    print("Incorrect values. ")
elif T_L<T_A:
    print("Check your values, Lectures taken can't be less than lectures attended")
else:
    per= (T_A*100)/T_L
    print("Total attendence Percentage is :", per)
    if per<75:
        print("You are not eligible for appearing in exam.")
        print("For appearing in exam your attendence must be 75%")
    elif per>=75:
        print("You are  eligible for appearing in exam.")
