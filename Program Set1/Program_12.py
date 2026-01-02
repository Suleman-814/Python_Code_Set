# Program to find factorial of a number using Recursion.

def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n * factorial(n-1)
print("Enter a number whose factorial is o be performed : ")
Number= int(input())
if Number<0:
    print("Factorial not possible ")
else:
    print("Factorial of", Number, "is", factorial(Number))
