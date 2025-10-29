# Program to find largest of three numbers

Number1=int(input("Enter Number1 : "))
Number2=int(input("Enter Number2 : "))
Number3=int(input("Enter Number3 : "))
if (Number1>Number2 ) and (Number1>Number3):
    Largest=Number1
    print("The Largest Number is ", Largest)
elif (Number2>Number1 ) and (Number2>Number3):
    Largest=Number2
    print("The Largest Number is ", Largest)
else:
    Largest=Number3
    print("The Largest Number is ", Largest)
