#WAP to find the larhest number from the given numbers.

def age():
    Number1=int(input("Enter Number1 : "))
    Number2=int(input("Enter Number2 : "))
    Number3=int(input("Enter Number3 : "))
    if Number1<0 or Number2<0 or Number3<0:
        print("No Negative")
    elif (Number1>Number2 ) and (Number1>Number3):
        Largest=Number1
        print("The Largest Number 1st :", Largest)
    elif (Number2>Number1 ) and (Number2>Number3):
        Largest=Number2
        print("The Largest Number 2nd :", Largest)
    elif (Number3>Number2 ) and (Number3>Number1):
        Largest=Number3
        print("The Largest Number 3rd :", Largest)
    else:
        ("Terminate")

age()        
