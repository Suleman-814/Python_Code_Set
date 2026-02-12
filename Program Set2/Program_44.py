#######################Exception Handling###################

#WAP to Perform Division of Two Numbers Using Exception Handling

try:
    num1=float(input("Enter a number:"))
    num2=float(input("Enter a number:"))
    Div=num1/num2
    print(f"Division of {num1} divide by {num2} is:",Div)
except ZeroDivisionError:
    print("Number cannot be divided by Zero!")
finally:
    print("Thank You")
    
