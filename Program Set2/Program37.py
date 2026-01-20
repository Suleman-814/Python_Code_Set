#WAP to check whether a triangle is isosceles or scalen.

def triangle():
    num1=float(input("Enter a number:"))
    num2=float(input("Enter a number:"))
    num3=float(input("Enter a number:"))
    if num1!=num2!=num3!=num1:
        print("scalen")
    else:
        if num1!=num2!=num3==num1 or num1!=num2==num3!=num1 or num1==num2!=num3!=num1:
            print("isosceles")
triangle()    
        
    
    